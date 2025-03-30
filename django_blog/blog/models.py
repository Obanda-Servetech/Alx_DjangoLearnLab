from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a blog post.
    """
    STATUS_CHOICES = (
        (True, "Published"),
        (False, "Draft"),
    )

    title = models.CharField(max_length=200, help_text="Enter the title of the blog post.")
    content = models.TextField(help_text="Write the content of the blog post here.")
    published_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the post was published.")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="posts",
        help_text="The author of the blog post. A user can have multiple posts."
    )
    status = models.BooleanField(choices=STATUS_CHOICES, default=False, help_text="Publish status of the post (Draft or Published).")

    class Meta:
        ordering = ["-published_date"]  # Latest posts appear first

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

