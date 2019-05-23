from django.urls import path
from .views import add_task_page

urlpatterns = [
    path('add/', add_task_page, name='add_task')
]