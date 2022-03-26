# Generated by Django 3.2.9 on 2022-03-23 06:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0009_promotionitem_over_image_text_color'),
        ('card', '0003_auto_20220313_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMenuItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('menu_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_projects.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]