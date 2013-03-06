from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('store', views.store, name="store"),
    path('<int:task_id>/complete', views.complete, name="complete"),
]