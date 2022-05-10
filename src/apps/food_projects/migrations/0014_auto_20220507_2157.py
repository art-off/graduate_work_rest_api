# Generated by Django 3.2.9 on 2022-05-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0013_auto_20220507_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='allowed_options',
            field=models.ManyToManyField(blank=True, to='food_projects.MenuOption'),
        ),
        migrations.AlterField(
            model_name='promotionitem',
            name='allowed_options',
            field=models.ManyToManyField(blank=True, to='food_projects.MenuOption'),
        ),
    ]
