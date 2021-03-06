# Generated by Django 3.2.7 on 2022-06-26 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_alter_shopunit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopunit',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.shopunit'),
        ),
        migrations.AlterField(
            model_name='shopunit',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
