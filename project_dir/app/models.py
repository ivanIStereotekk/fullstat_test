"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

import uuid

import requests
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser,User

# ---ORM Models:
class Person(AbstractUser):
    """
    "Person" who is ordinary service user - Django Authentication System
    """
    GENDERS = (('m', 'Male'), ('*', 'None'), ('w', 'Woman'))
    gender = models.CharField(max_length=4, default='*', choices=GENDERS, verbose_name='Gender')
    biography = models.TextField(max_length=555,null=True, verbose_name='Biography')
    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('person_id', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Registred User'
        verbose_name_plural = 'Registred User\'s'
        ordering = ['username','email']


class Post(models.Model):
    """
    POST'S of published posts
    """
    uuid_tag = models.UUIDField(primary_key=False, default=uuid.uuid4, null=True)
    title = models.TextField(max_length=80, verbose_name='Title of Article')
    discription = models.TextField(null=True, max_length=250, verbose_name='Short description')
    content = models.TextField(verbose_name='Text body')
    req_count = models.IntegerField(default=0, null=True, verbose_name='Reading counter')
    slug = models.SlugField(default=None, unique=True, db_index=True, max_length=90, verbose_name='Url-slug')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    rating = models.IntegerField(null=True, verbose_name='Rating Of publication')
    author = models.ForeignKey(Person, blank=True, null=True, on_delete=models.PROTECT,verbose_name='Author_ID')


    def increment(self):  # increments view counter
        self.req_count += 1
        return self.req_count

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Publication or Post'
        verbose_name_plural = 'Publications'
        ordering = ['-created_at']


class Bookmark(models.Model):
    """
    Person's(User's) bookmarks set linked model
    """
    posts = models.ManyToManyField('Post', verbose_name='Subscribed posts')
    bookmark_name = models.TextField(max_length=80, verbose_name='Bookmark title')
    owner = models.ForeignKey(Person, models.SET_NULL,blank=True,null=True,related_name='owner', verbose_name='Owner')

    def __str__(self):
        return str(self.owner)


class Link(models.Model):
    """
    "Link" model which gives to user(person) some options like
    """
    CHOOSE = (('-0', 'Minus'), ('0', 'Null'), ('1', 'Plus One'))
    post = models.ForeignKey(Post,on_delete=models.DO_NOTHING,verbose_name='Which_post')
    estimation = models.CharField(max_length=4, choices=CHOOSE, verbose_name='My estimation')
    is_bookmarked = models.BooleanField(default=False,verbose_name='Is Bookmarked')
    like = models.BooleanField(default=False, verbose_name='Like')
    disslike = models.BooleanField(default=False, verbose_name='Disslike')
    whos_link = models.ForeignKey(Person, models.PROTECT, blank=True, null=True, related_name='user', verbose_name='Whos_link')

    def __str__(self):
        return str(self.pk)
