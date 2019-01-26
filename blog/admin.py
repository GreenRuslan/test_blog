from django.contrib import admin
from .models import Post, Comments

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text'[:40], 'user')


admin.site.register(Post)
admin.site.register(Comments, CommentsAdmin)