# Generated by Django 3.2.12 on 2023-06-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0018_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]