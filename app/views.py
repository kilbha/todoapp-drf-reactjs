from django.shortcuts import render
from app.models import Task
from app.api.serializer import TaskSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

@api_view(['GET'])

def apiOverView(request):
    api_urls = {
        "List":"/task-list/",
        'Detail View':"/task-detail/<str:pk>/",
        "Create":'/task-create/',
        'update':'/task-update/<str:pk>/',
        "Delete":'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])    
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])    
def taskCreate(request):    
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])    
def taskUpdate(request,pk):    
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    
    
@api_view(['DELETE'])    
def taskDelete(request,pk):    
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Deleted Successfully")