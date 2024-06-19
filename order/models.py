from django.db import models
from pos_manage.models import Food

# Create your models here.
class Order(models.Model):
    ID = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(null=True)
    is_pay = models.BooleanField(default=False)
    food_amount = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    table_id = models.IntegerField(default=0)
    comment = models.CharField(max_length=50, default='')
    # staff = models.ForeignKey(
    #     'Staff', on_delete=models.DO_NOTHING)     # 当时负责的员工

    def __str__(self):
        return 'Order ' + str(self.ID)
    
class OrderItem(models.Model):
    orderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    foodID = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=1)
    sum_price = models.FloatField(default=0)
    status = models.IntegerField(default=0, choices=(   # (0, '尚未接單'), (1, '準備餐點'), (2, '等待上菜'), (3, '上菜完成')
        (0, '尚未接單'), (1, '準備餐點'), (2, '等待上菜'), (3, '上菜完成')))
    start_cook_time = models.TimeField(null=True)
    end_cook_time = models.TimeField(null=True)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.foodID.title + ' in Order ' + str(self.orderID.ID)