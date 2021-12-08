# Generated by Django 3.2.7 on 2021-12-08 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profesional', '0002_auto_20211121_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaprofesional',
            name='nombre',
        ),
        migrations.AddField(
            model_name='personaprofesional',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profesional', to=settings.AUTH_USER_MODEL),
        ),
    ]
