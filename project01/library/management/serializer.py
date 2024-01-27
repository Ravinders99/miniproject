from rest_framework import serializers
from .models import Books, Magazines
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
class MagazinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazines
        fields = '__all__'