# Generated by Django 3.2.2 on 2021-05-31 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='airtime',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='bonga',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='bundles',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='mpesa',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='okoa_bal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='okoa_limit',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='okoa_taken',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='sms',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='user_num',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='accounts', serialize=False, to='users.regusers'),
        ),
    ]
