from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed-stories/', views.feed_stories, name='feed_stories'),
    path('feed-stories/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.feed_story, name='feed_story'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:id>/', views.task, name='task'),
]
