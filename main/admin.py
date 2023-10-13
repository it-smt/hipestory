from django.contrib import admin

from main.models import Story, StoryComment, Task, TaskCommentAnswer


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated', 'is_active', 'status')
    list_filter = ('created', 'updated', 'is_active', 'status')
    fields = (('title', 'slug'), 'author', 'body', 'is_active', 'status')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)


@admin.register(StoryComment)
class StoryCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskCommentAnswer)
class TaskCommentAnswerAdmin(admin.ModelAdmin):
    pass
