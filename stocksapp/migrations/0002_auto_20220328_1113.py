# Generated by Django 3.1.7 on 2022-03-28 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocksapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trade',
            new_name='Stocks',
        ),
    ]