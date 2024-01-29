from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer
from .permissions import AdminOrReadOnly

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] #Object level permissions
    permission_classes = [AdminOrReadOnly] #Custom permission class
    queryset = Course.objects.all()
    serializer_class = CourseSerializer