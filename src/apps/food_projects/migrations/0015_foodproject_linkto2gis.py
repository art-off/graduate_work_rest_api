# Generated by Django 3.2.9 on 2022-05-14 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0014_auto_20220507_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproject',
            name='linkTo2Gis',
            field=models.URLField(default='https://go.2gis.com/oxqsun'),
            preserve_default=False,
        ),
    ]
