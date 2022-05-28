import uuid

from django.db import models



from django.urls import reverse
class Person(models.Model):
    '''
    Person who are ordinary service user
    '''
    username = models.TextField(max_length=100,verbose_name='Username')
    email = models.EmailField(null=True, verbose_name='Email')
    password = models.TextField(null=True, verbose_name='Password')
    token = models.TextField(max_length=555,verbose_name='JWT')
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('person_id', kwargs={'pk': self.pk})

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
from django.urls import reverse

class Post(models.Model):
    '''
    POSTS of published posts
    '''
    uuid_tag = models.UUIDField(primary_key=False,default=uuid.uuid4,null=True)
    title = models.TextField(null=True,verbose_name='Title of Article')
    author = models.ForeignKey(Person,on_delete=models.PROTECT,null=True,verbose_name='Author')
    discription = models.TextField(null=True,verbose_name='Short description')
    content = models.TextField(verbose_name='Text')
    req_count = models.IntegerField(null=True,verbose_name='Counter watched times')
    like = models.IntegerField(null=True,verbose_name='Like')
    disslike = models.IntegerField(null=True,verbose_name='Disslike')
    slag = models.SlugField(null=True,max_length=100,verbose_name='Slag')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created')
    bookmarks = models.ManyToManyField('Bookmark',through='Link',through_fields=('posts','bookmark'),null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-created_at']

class Bookmark(models.Model):
    '''
    user's bookmarks set linked model
    '''
    person = models.ForeignKey(Person,on_delete=models.PROTECT,verbose_name='Bookmark')
    def __str__(self):
        return self.person
class Link(models.Model):
    '''
    Link model trough set of records bookmarks and posts - ManyToMany
    '''
    posts = models.ForeignKey('Post',on_delete=models.CASCADE)
    bookmark = models.ForeignKey('Bookmark',on_delete=models.CASCADE,verbose_name='link_bookmark')
    def __str__(self):
        return self.pk
