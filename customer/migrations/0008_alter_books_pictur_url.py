# Generated by Django 3.2.4 on 2021-06-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_books_pictur_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pictur_url',
            field=models.CharField(max_length=240, verbose_name='pictur_url'),
        ),
    ]
