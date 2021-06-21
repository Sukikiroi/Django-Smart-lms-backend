# Generated by Django 3.2.4 on 2021-06-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=240, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.CharField(max_length=240, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=240, verbose_name='title'),
        ),
    ]
