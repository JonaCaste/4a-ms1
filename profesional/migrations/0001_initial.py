# Generated by Django 3.2.7 on 2021-11-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDocumento', models.CharField(max_length=64)),
                ('numeroDocumento', models.IntegerField()),
                ('nombre', models.CharField(max_length=64)),
                ('perfil', models.CharField(max_length=64)),
            ],
        ),
    ]
