# Generated by Django 3.1.4 on 2020-12-14 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0004_auto_20201213_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='truck',
            name='owner',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck', to=settings.AUTH_USER_MODEL),
        ),
    ]
