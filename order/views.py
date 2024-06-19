from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from pos_manage.models import Foodtype,Food, Table
from .models import Order, OrderItem

import json


# Create your views here.
@csrf_exempt
def order(request):
    if request.method == "GET":
        foodList = Food.objects.all()
        foodTypeList = Foodtype.objects.all()
        tableList = Table.objects.all()
        return render(
            request,
            'order/order.html',
            {
                'foodList': foodList,
                'foodTypeList': foodTypeList,
                'tableList': tableList,
            }
        )
    elif request.method == "POST":
        foodList = json.loads(request.POST.get('foodList'))
        table_id = request.POST.get('table')

        # 創建訂單 填寫基本信息
        new_order = Order(table_id=table_id, is_pay=False)
        staff_in_charge = Table.objects.get(pk=table_id).staff
        new_order.staff = staff_in_charge   # 當前桌邊負責人
        new_order.save()

        # 先 save 再獲取ID
        order_id = new_order.ID
        food_amount = 0
        total_price = 0

        for food in foodList:
            curFood = Food.objects.get(pk=food['id'])
            price = curFood.price
            sum_price = price * food['amount']
            curFood.amount -= food['amount']
            curFood.save()

            food_amount += food['amount']
            total_price += sum_price

            OrderItem.objects.create(
                orderID=new_order,
                foodID=curFood,
                amount=food['amount'],
                sum_price=sum_price
            )
        # 訂單物品總數、價格
        new_order.food_amount = food_amount
        new_order.total_price = total_price
        new_order.save()

        return HttpResponse(json.dumps({
            'order_id': order_id
        }))
    
# 帳單詳情
def QueryOrder(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except:
        return HttpResponse('無此訂單！')

    foodList = Food.objects.filter(orderitem__orderID__ID=order_id)

    with connection.cursor() as cursor:
        SELECT_COL = 'OrderSystem_food.ID ID, OrderSystem_food.title title, OrderSystem_orderitem.amount amount'
        SELECT_COL += ', OrderSystem_orderitem.sum_price '
        SELECT_COL += ', OrderSystem_orderitem.start_cook_time '
        SELECT_COL += ', OrderSystem_orderitem.end_cook_time '
        SELECT_FROM = 'OrderSystem_food, OrderSystem_orderitem '
        SELECT_WHERE = 'OrderSystem_food.ID=OrderSystem_orderitem.foodID_id '
        SELECT_WHERE += ' and OrderSystem_orderitem.orderID_id={0}'.format(
            order_id)
        cursor.execute(
            f'select {SELECT_COL} from {SELECT_FROM} where {SELECT_WHERE}')
        foodJsonList = dictfetchall(cursor)

    return render(request, 'QueryOrder.html', {
        'order': order,
        'foodList': foodJsonList,
    })


def check(request):
    return render(request, 'order/check.html')

# ----------------------------------------------------------------函數----------------------------------------------------------------
def dictfetchall(cursor):
    '''輔助函數 數據庫查詢結果轉換成 json/dict'''
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]