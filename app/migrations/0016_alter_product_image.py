# Generated by Django 3.2.7 on 2024-03-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/images/bakery/pimg'),
        ),
    ]
