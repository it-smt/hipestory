from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import User


class StoryPublishedManager(models.Manager):
    def queryset(self):
        super().queryset().filter(status=Story.Status.PUBLISHED, is_active=True)


class Story(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Опубликовано'
        DRAFT = 'DF', 'Черновик'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique_for_date='created')
    body = models.TextField(verbose_name='Содержание')
    created = models.DateField(verbose_name='Создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Изменено', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активная?', default=True)
    status = models.CharField(max_length=2, verbose_name='Статус', choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = StoryPublishedManager()

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
        ordering = ('-updated',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:feed_story', args=[self.created.year,
                                                self.created.month,
                                                self.created.day,
                                                self.slug])

    def get_formatted_body(self):
        return self.body.split('\r\n')


class StoryComment(models.Model):
    story = models.ForeignKey(Story, verbose_name='История', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='story_comments')
    date = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
    body = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Комментарий к истории'
        verbose_name_plural = 'Комментарии к историям'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.user.username} - {self.story.title}'

    def get_formatted_body(self):
        return self.body.split('\r\n')


class TaskPublishedManager(models.Manager):
    def queryset(self):
        super().queryset().filter(status=Task.Status.PUBLISHED, is_active=True)


class Task(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Опубликовано'
        DRAFT = 'DF', 'Черновик'

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    body = models.TextField(verbose_name='Содержание')
    created = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активная?', default=True)
    status = models.CharField(verbose_name='Статус', max_length=2, choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = TaskPublishedManager()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_formatted_body(self):
        return self.body.split('\r\n')


class TaskCommentAnswer(models.Model):
    task = models.ForeignKey(verbose_name='Задание', to=Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE, related_name='task_comments')
    date = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)
    body = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Ответ на задание'
        verbose_name_plural = 'Ответы на задания'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.user.username} - {self.task.title}'

    def get_formatted_body(self):
        return self.body.split('\r\n')
