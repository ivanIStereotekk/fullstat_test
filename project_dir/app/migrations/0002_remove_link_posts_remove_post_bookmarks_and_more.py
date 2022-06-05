# Generated by Django 4.0.4 on 2022-05-31 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='posts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='bookmarks',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='posts',
            field=models.ManyToManyField(to='app.post', verbose_name='Subscribed posts'),
        ),
        migrations.AddField(
            model_name='link',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.post'),
        ),
        migrations.AlterField(
            model_name='link',
            name='bookmark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.bookmark'),
        ),
    ]