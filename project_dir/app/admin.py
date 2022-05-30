from django.contrib import admin

from .models  import Post ,Person, Link, Bookmark

class Post_Admin(admin.ModelAdmin):
    list_display = ('title','author','req_count','discription','created_at',)
    list_display_links = ('title','author')
    search_fields = ('content','title','author','created_at')
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post,Post_Admin)

class Person_Admin(admin.ModelAdmin):
    list_display = ('username','email','password','token')
    list_display_links = ('username','email',)
    search_fields = ('username','email',)
admin.site.register(Person,Person_Admin)

class Bookmark_Admin(admin.ModelAdmin):
    list_display = ('person','bookmark_name',)
admin.site.register(Bookmark,Bookmark_Admin)

class Link_Admin(admin.ModelAdmin):
    list_display = ('bookmark','is_bookmarked','posts',)
admin.site.register(Link,Link_Admin)