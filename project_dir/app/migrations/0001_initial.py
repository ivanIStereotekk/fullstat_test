# Generated by Django 4.0.4 on 2022-05-30 13:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark_name', models.TextField(max_length=80, null=True, verbose_name='Bookmark title')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimation', models.CharField(choices=[('-0', 'Minus'), ('0', 'Null'), ('1', 'Plus One')], max_length=4, verbose_name='My estimation')),
                ('is_bookmarked', models.BooleanField(default=True, null=True, verbose_name='Is Bookmarked')),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bookmark', verbose_name='link_bookmark')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('password', models.TextField(null=True, verbose_name='Password')),
                ('token', models.TextField(max_length=555, verbose_name='JWT')),
            ],
            options={
                'verbose_name': 'Registred User',
                'verbose_name_plural': "Registred User's",
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_tag', models.UUIDField(default=uuid.uuid4, null=True)),
                ('title', models.TextField(max_length=80, null=True, verbose_name='Title of Article')),
                ('discription', models.TextField(max_length=250, null=True, verbose_name='Short description')),
                ('content', models.TextField(verbose_name='Text body')),
                ('req_count', models.IntegerField(default=0, null=True, verbose_name='Reading counter')),
                ('like', models.IntegerField(null=True, verbose_name='Like')),
                ('disslike', models.IntegerField(null=True, verbose_name='Disslike')),
                ('slug', models.SlugField(max_length=90, null=True, unique=True, verbose_name='Url-slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('rating', models.IntegerField(null=True, verbose_name='Rating Of publication')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.person', verbose_name='Author')),
                ('bookmarks', models.ManyToManyField(through='app.Link', to='app.bookmark')),
            ],
            options={
                'verbose_name': 'Publication or Post',
                'verbose_name_plural': 'Publications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='link',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to='app.person', verbose_name='Bookmark'),
        ),
    ]