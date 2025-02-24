from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
<form method="POST" action="{% url 'book-create' %}">
    {% csrf_token %}
    <label for="title">Title:</label>
    <input type="text" name="title" id="title" required>
    <button type="submit">Submit</button>
</form>
