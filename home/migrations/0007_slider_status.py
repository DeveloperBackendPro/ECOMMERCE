# Generated by Django 4.0.1 on 2022-02-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='status',
            field=models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud Emas')], default='True', max_length=15),
        ),
    ]
