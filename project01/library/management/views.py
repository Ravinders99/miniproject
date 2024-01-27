from django.shortcuts import render
from .models import Books, Magazines
from .serializer import BooksSerializer , MagazinesSerializer
from rest_framework import viewsets, permissions
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]

class MagazinesViewSet(viewsets.ModelViewSet):
    queryset = Magazines.objects.all()
    serializer_class = MagazinesSerializer
    permission_classes = [permissions.IsAuthenticated]
