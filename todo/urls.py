
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('login',views.user_login),
    path('todo/',views.todo, name='todo'),
    path('todo/edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
