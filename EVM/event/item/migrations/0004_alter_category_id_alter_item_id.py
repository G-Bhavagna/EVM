# Generated by Django 4.1.7 on 2023-03-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20230307_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
