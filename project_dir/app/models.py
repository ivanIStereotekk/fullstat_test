import uuid
from django.urls import reverse
from django.db import models
#---ORM Models:
class Person(models.Model):
    '''
    Person who is ordinary service user
    '''
    username = models.TextField(max_length=100,verbose_name='Username')
    email = models.EmailField(null=True, verbose_name='Email')
    password = models.TextField(null=True, verbose_name='Password')
    token = models.TextField(max_length=555,verbose_name='JWT')
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('person_id', kwargs={'pk': self.pk})
    class Meta:
        verbose_name = 'Registred User'
        verbose_name_plural = 'Registred User\'s'
        ordering = ['username']



class Post(models.Model):
    '''
    POSTS of published posts
    '''
    uuid_tag = models.UUIDField(primary_key=False,default=uuid.uuid4,null=True)
    title = models.TextField(null=True,max_length=80,verbose_name='Title of Article')
    author = models.ForeignKey(Person,on_delete=models.PROTECT,null=True,verbose_name='Author')
    discription = models.TextField(null=True,max_length=250,verbose_name='Short description')
    content = models.TextField(verbose_name='Text body')
    req_count = models.IntegerField(default=0,null=True,verbose_name='Reading counter')
    like = models.IntegerField(null=True,verbose_name='Like')
    disslike = models.IntegerField(null=True,verbose_name='Disslike')
    slug = models.SlugField(null=True,unique=True,db_index=True,max_length=90,verbose_name='Url-slug')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created')
    bookmarks = models.ManyToManyField('Bookmark',through='Link',through_fields=('posts','bookmark'))
    rating = models.IntegerField(null=True,verbose_name='Rating Of publication')
    def increment(self):
        self.req_count +=1
        return self.req_count
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    class Meta:
        verbose_name = 'Publication or Post'
        verbose_name_plural = 'Publications'
        ordering = ['-created_at']

class Bookmark(models.Model):
    '''
    user's bookmarks set linked model
    '''
    bookmark_name = models.TextField(null=True,max_length=80,verbose_name='Bookmark title')
    person = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='user',verbose_name='Bookmark')
    def __str__(self):
        return str(self.person)
class Link(models.Model):
    '''
    Link model trough set of records bookmarks and posts - ManyToMany
    '''
    CHOOSE = (('-0','Minus'),('0','Null'),('1','Plus One'))
    posts = models.ForeignKey('Post',on_delete=models.CASCADE)
    bookmark = models.ForeignKey('Bookmark',on_delete=models.CASCADE,verbose_name='link_bookmark')
    estimation = models.CharField(max_length=4,choices=CHOOSE,verbose_name='My estimation')
    is_bookmarked = models.BooleanField(default=True,null=True,verbose_name='Is Bookmarked')
    def __str__(self):
        return str(self.pk)

class Manager_Set(models.QuerySet):
    def get_queryset(self):
        pass
    class Meta:
        verbose_name = 'Related records'
        verbose_name_plural = 'Related records\'s'
        ordering = ['username']