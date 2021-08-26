# Generated by Django 3.2.6 on 2021-08-26 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0003_snack_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='snack',
            name='purchaser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]