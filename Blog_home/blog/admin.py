from django.contrib import admin

from .models import Note, Comment

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "public", "update_at", "create_at", "id")

    # fields =
    # readonly_fields =

    search_fields = ['title', "message"]

    list_filter = ('public', 'author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
