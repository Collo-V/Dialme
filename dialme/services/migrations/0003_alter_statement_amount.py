# Generated by Django 3.2.2 on 2021-06-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_statement_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
