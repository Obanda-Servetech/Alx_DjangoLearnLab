from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
["class CustomUser(AbstractUser):", "date_of_birth", "profile_photo"]

["class CustomUserManager(BaseUserManager):", "create_user", "create_superuser"]

# Defining custom permissions in models
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view articles"),
            ("can_create", "Can create articles"),
            ("can_edit", "Can edit articles"),
            ("can_delete", "Can delete articles"),
        ]


