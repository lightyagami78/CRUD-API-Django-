# Generated by Django 4.1.1 on 2022-11-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0002_alter_report_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='price',
            field=models.IntegerField(),
        ),
    ]