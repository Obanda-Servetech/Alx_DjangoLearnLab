from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework
["from django_filters import rest_framework"]
"from django_filters import rest_framework"
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from rest_framework import filters, generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """Retrieve all books with filtering, searching, and ordering."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define filter fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Enable search functionality
    search_fields = ['title', 'author__name']

    # Allow ordering by title and publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
["from django_filters import rest_framework"]