from django.urls import path , include
from . import views
urlpatterns = [

    path('books/', views.BooksViewSet.as_view({'get': 'list'})),
    path('magazines/', views.MagazinesViewSet.as_view({'get': 'list'}))
]
