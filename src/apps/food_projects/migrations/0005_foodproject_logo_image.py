# Generated by Django 3.2.9 on 2022-03-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_projects', '0004_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodproject',
            name='logo_image',
            field=models.ImageField(default='Screenshot_2022-02-28_at_14.48.13.png', upload_to=''),
            preserve_default=False,
        ),
    ]