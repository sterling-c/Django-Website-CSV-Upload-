# Generated by Django 3.0.2 on 2020-05-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='cpu',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='opSys',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='storageMem',
            field=models.CharField(max_length=50),
        ),
    ]
