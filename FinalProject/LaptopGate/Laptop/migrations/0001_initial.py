# Generated by Django 3.0.2 on 2020-05-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=25)),
                ('product_type', models.CharField(max_length=25)),
                ('length', models.DecimalField(decimal_places=1, max_digits=6)),
                ('screenRes', models.CharField(max_length=50)),
                ('cpu', models.CharField(max_length=25)),
                ('ram', models.IntegerField()),
                ('storageMem', models.CharField(max_length=25)),
                ('gpu', models.CharField(max_length=50)),
                ('opSys', models.CharField(max_length=25)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
