# Generated by Django 3.2.9 on 2022-05-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0018_menuitemtype_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproject',
            name='appstore_api_key',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodproject',
            name='playmarket_api_key',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
