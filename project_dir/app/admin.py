"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

from django.contrib import admin

from .models  import Post ,Person, Link, Bookmark

class Post_Admin(admin.ModelAdmin):
    list_display = ('title','author','req_count','discription','created_at',)
    list_display_links = ('title','author')
    search_fields = ('content','title','author','created_at')
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post,Post_Admin)

class Person_Admin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user',)
admin.site.register(Person,Person_Admin)

class Bookmark_Admin(admin.ModelAdmin):
    list_display = ('username','bookmark_name',)
    list_display_links = ('username',)
admin.site.register(Bookmark,Bookmark_Admin)

class Link_Admin(admin.ModelAdmin):
    list_display = ('is_bookmarked','post','estimation','like','disslike',)
    list_display_links = ('post','like','disslike',)
admin.site.register(Link,Link_Admin)