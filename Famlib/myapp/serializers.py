import rest_framework
from rest_framework import serializers
from .models import Library,Users,Book,Message

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
        model=Book
        exclude = ('id','date','username')
        # read_only_fields = ('id')