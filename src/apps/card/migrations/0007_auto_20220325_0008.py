# Generated by Django 3.2.9 on 2022-03-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20220323_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermenuitem',
            name='menu_item',
        ),
        migrations.RemoveField(
            model_name='orderpromotions',
            name='promotion',
        ),
    ]
