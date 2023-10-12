from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from main.forms import CommentForm
from main.models import Story, Task, StoryComment, TaskCommentAnswer


def index(request):
    return render(request, 'index.html')


def feed_stories(request):
    stories = Story.published.all()
    context = {'stories': stories}
    return render(request, 'main/feed-stories.html', context)


def feed_story(request, year, month, day, slug):
    story = get_object_or_404(Story, status=Story.Status.PUBLISHED, is_active=True, created__year=year,
                              created__month=month, created__day=day, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = request.user
        if user.is_authenticated:
            body = request.POST.get('body', '')
            if body:
                comment = StoryComment()
                comment.user = user
                comment.story = story
                comment.body = body
                comment.save()
                messages.success(request, 'Комментарий успешно добавлен!')
                return redirect(story.get_absolute_url())
    else:
        form = CommentForm()
    context = {'story': story, 'form': form}
    return render(request, 'main/feed-story.html', context)


@login_required
def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main/tasks.html', context)


@login_required
def task(request, id):
    task = get_object_or_404(Task, pk=id, is_active=True, status=Task.Status.PUBLISHED)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = request.user
        if user.is_authenticated:
            body = request.POST.get('body', '')
            if body:
                comment = TaskCommentAnswer()
                comment.user = user
                comment.task = task
                comment.body = body
                comment.save()
                messages.success(request, 'Комментарий успешно добавлен!')
                return redirect(reverse('main:task', args=[task.id]))
    else:
        form = CommentForm()
    context = {'task': task, 'form': form}
    return render(request, 'main/task.html', context)
