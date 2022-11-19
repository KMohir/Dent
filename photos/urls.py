from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('add-team/', views.addTeam, name='add_team'),
    path('update-photo/<str:pk>/', views.UpdatePhoto, name='update_photo'),
    path('update-team/<str:pk>/', views.UpdateTeam, name='update_team'),
    path('delete-photo/<str:pk>/', views.DeletePhoto, name='delete_photo'),
    path('delete-team/<str:pk>/', views.DeleteTeam, name='delete_team'),
    path('delete-category/<str:pk>/', views.DeleteCategory, name='delete_category'),

]
