import rest_framework
from rest_framework import serializers
from .models import*

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('name', 'library_id', 'email')

class UserSerializer(serializers.ModelSerializer):
    libraryid = serializers.UUIDField(format='hex')
    class Meta:
        model=Users
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        # exclude = ('id','date','username')
        # read_only_fields = ('id')
        fields='__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'