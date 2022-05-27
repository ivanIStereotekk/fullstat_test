import uuid

from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    '''
    Person who are related with django.User class
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Username')
    token = models.TextField(max_length=555,verbose_name='JWT')
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('user_id', kwargs={'pk': self.pk})

'''
По Статье хранится следующая информация
- Артикул статьи (число)
- Заголовок статьи транслитом (строка)
- Заголовок статьи (строка)
- Автор (строка)
- Краткое содержание (строка | макс. 250 символов)
- Содержание (строка)
- Количество просмотров (число)
- В избранном (true/false)
- Моя оценка (-1, 0, 1)
- Рейтинг (число)
'''

class Post(models.Model):
    '''
    POSTS of published posts
    '''
    uuid_tag = models.UUIDField(primary_key=False,default=uuid.uuid4)
    title = models.TextField(null=True,verbose_name='Title')
    autor = models.ForeignKey(Person,on_delete=models.PROTECT,verbose_name='Author')
    discription = models.TextField(null=True,verbose_name='Short description')
    content = models.TextField(verbose_name='Text')
    req_count = models.IntegerField(null=True,verbose_name='Counter')
    like = models.IntegerField(null=True,verbose_name='Like')
    disslike = models.IntegerField(null=True,verbose_name='Disslike')
    slag_field = models.SlugField(max_length=66,verbose_name='Slag')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created')
    bookmarks = models.ManyToManyField('Bookmark',through='Link',through_fields=('posts','bookmark'),null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_id', kwargs={'pk': self.pk})


class Bookmark(models.Model):
    '''
    user's bookmarks set linked model
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Bookmark')

class Link(models.Model):
    '''
    Link model trough set of records bookmarks and posts - ManyToMany
    '''
    posts = models.ForeignKey('Post',on_delete=models.CASCADE)
    bookmark = models.ForeignKey('Bookmark',on_delete=models.CASCADE,verbose_name='link_bookmark')
