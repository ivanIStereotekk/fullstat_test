# Generated by Django 4.0.4 on 2022-06-05 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_person_options_remove_bookmark_person_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='token',
        ),
        migrations.AddField(
            model_name='person',
            name='additional',
            field=models.TextField(max_length=555, null=True, verbose_name='Additional Field'),
        ),
    ]