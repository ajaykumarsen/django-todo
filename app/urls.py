from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoView, name='home'),
    path('addTodo/', views.addTodo, name='add-todo'),
    path('deleteTodo/<int:todo_id>', views.deleteTodo, name='delete-todo'),

]