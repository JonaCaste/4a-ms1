# Generated by Django 3.2.7 on 2021-11-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_personacliente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personacliente',
            name='email',
        ),
    ]
