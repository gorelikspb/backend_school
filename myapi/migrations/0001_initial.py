# Generated by Django 3.2.7 on 2022-06-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('OFFER', 'OFFER'), ('CATEGORY', 'CATEGORY')], max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.shopunit')),
            ],
        ),
    ]
