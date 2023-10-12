from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/change-avatar', views.change_avatar, name='change_avatar'),
    # path('profile/crop-avatar', views.crop_avatar, name='crop_avatar'),
    path('profile/add-avatar', views.add_avatar, name='add_avatar'),
    path('profile/delete-avatar', views.delete_avatar, name='delete_avatar'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/new-story/', views.new_story, name='new_story'),
]
