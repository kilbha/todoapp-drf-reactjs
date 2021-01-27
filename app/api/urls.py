from django.urls import path

from app.views import apiOverView,tasklist,taskDetail,taskCreate,taskDelete,taskUpdate
urlpatterns = [
    path('',apiOverView,name='api-list'),
    path('task-list/',tasklist,name='task-list'),
    path('task-detail/<str:pk>/',taskDetail,name='task-detail'),
    path('task-create/',taskCreate,name='task-create'),
    path('task-update/<str:pk>/',taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',taskDelete,name='task-delete'),
]