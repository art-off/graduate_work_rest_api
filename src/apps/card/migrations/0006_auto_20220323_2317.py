# Generated by Django 3.2.9 on 2022-03-23 16:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0009_promotionitem_over_image_text_color'),
        ('card', '0005_alter_ordermenuitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu_items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='promotions',
        ),
        migrations.AlterField(
            model_name='ordermenuitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.order'),
        ),
        migrations.CreateModel(
            name='OrderPromotions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.order')),
                ('promotion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_projects.promotionitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]