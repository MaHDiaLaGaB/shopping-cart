# Generated by Django 4.0.3 on 2022-03-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
