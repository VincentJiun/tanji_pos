# Generated by Django 5.0.4 on 2024-06-19 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pos_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('pay_time', models.DateTimeField(null=True)),
                ('is_pay', models.BooleanField(default=False)),
                ('food_amount', models.IntegerField(default=0)),
                ('total_price', models.FloatField(default=0)),
                ('table_id', models.IntegerField(default=0)),
                ('comment', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('sum_price', models.FloatField(default=0)),
                ('status', models.IntegerField(choices=[(0, '后厨未接单'), (1, '后厨在准备'), (2, '等待上菜'), (3, '上菜完成')], default=0)),
                ('start_cook_time', models.TimeField(null=True)),
                ('end_cook_time', models.TimeField(null=True)),
                ('comment', models.CharField(max_length=50)),
                ('foodID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pos_manage.food')),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
