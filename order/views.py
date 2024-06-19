from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pos_manage.models import Foodtype,Food
from .models import Order, OrderItem

import json


# Create your views here.
@csrf_exempt
def order(request):
    if request.method == "GET":
        foodList = Food.objects.all()
        foodTypeList = Foodtype.objects.all()
        # tableList = Staff_Table.objects.all()
        return render(
            request,
            'order/order.html',
            {
                'foodList': foodList,
                'foodTypeList': foodTypeList,
                # 'tableList': tableList,
            }
        )
    elif request.method == "POST":
        foodList = json.loads(request.POST.get('foodList'))
        table_id = request.POST.get('table')

        # 创建订单 填写基本信息
        new_order = Order(table_id=table_id, is_pay=False)
        # staff_in_charge = Staff_Table.objects.get(pk=table_id).staff
        # new_order.staff = staff_in_charge   # 当前桌子的负责人
        new_order.save()

        # 先 save 再获取 ID
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
        # 订单的物品总数、总价
        new_order.food_amount = food_amount
        new_order.total_price = total_price
        new_order.save()

        return HttpResponse(json.dumps({
            'order_id': order_id
        }))
    
# def order(request):
#     return render(request, 'order/order.html')

def check(request):
    return render(request, 'order/check.html')