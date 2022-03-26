# Generated by Django 3.2.9 on 2022-03-24 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0009_promotionitem_over_image_text_color'),
        ('card', '0009_lolkekmodel_lol_kek_field'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LolKekModel',
        ),
        migrations.AddField(
            model_name='ordermenuitem',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_projects.menuitem'),
        ),
        migrations.AddField(
            model_name='orderpromotions',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_projects.promotionitem'),
        ),
    ]