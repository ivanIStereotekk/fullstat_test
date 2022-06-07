# Generated by Django 4.0.4 on 2022-06-07 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='whos_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Whos_link'),
        ),
        migrations.AlterField(
            model_name='link',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.post', verbose_name='Which_post'),
        ),
    ]
