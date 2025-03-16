from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """Retrieve all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """Create a new book (restricted to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """Update an existing book (restricted to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """Delete a book (restricted to authenticated users)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
["from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"]