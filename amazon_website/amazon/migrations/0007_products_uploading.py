# Generated by Django 5.0.4 on 2024-04-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0006_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='uploading',
            field=models.IntegerField(default=1),
        ),
    ]