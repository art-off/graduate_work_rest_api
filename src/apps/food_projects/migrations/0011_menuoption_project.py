# Generated by Django 3.2.9 on 2022-05-07 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0010_auto_20220507_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuoption',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='food_projects.foodproject'),
            preserve_default=False,
        ),
    ]
