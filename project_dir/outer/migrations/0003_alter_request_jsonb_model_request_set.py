# Generated by Django 4.0.4 on 2022-06-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outer', '0002_rename_request_jsonb_request_jsonb_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_jsonb_model',
            name='request_set',
            field=models.CharField(max_length=1000, verbose_name='Text'),
        ),
    ]