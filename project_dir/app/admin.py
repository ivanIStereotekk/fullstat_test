from django.contrib import admin

from .models  import Post

class Post_Admin(admin.ModelAdmin):
    list_display = ('title','author','created_at')
    list_display_links = ('title','author')
    search_fields = ('content','title','author')

admin.site.register(Post,Post_Admin)