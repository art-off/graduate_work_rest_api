# Generated by Django 3.2.9 on 2022-03-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0006_promotionitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproject',
            name='address',
            field=models.CharField(default='lolKek address', max_length=240),
            preserve_default=False,
        ),
    ]
