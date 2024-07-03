from rest_framework import serializers
from .models import *

class TodoListSeializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['titel']



class TodoDetailSeializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'