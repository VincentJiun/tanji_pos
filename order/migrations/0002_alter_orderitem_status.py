# Generated by Django 5.0.4 on 2024-06-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.IntegerField(choices=[(0, '尚未接單'), (1, '準備餐點'), (2, '等待上菜'), (3, '上菜完成')], default=0),
        ),
    ]
