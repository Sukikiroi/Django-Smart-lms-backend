# Generated by Django 3.2.4 on 2021-06-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210618_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=240, verbose_name='message'),
        ),
    ]