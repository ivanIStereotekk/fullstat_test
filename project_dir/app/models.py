from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    login = models.TextField(max_length=100)
    token = models.TextField(max_length=555)
    #class Meta:
        #uniq_together = ('email','login')


class Post(models.Model):
    title = models.TextField(null=True)
    autor = models.ForeignKey(Person,on_delete=models.PROTECT)
    discription = models.TextField(null=True)
    content = models.TextField(max_length=3000)
    req_count = models.IntegerField()
    like = models.IntegerField()
    disslike = models.IntegerField()
    slag_field = models.CharField(max_length=1000)
    #class Meta:
        #uniq_together = ('title','slag_field')
