from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),  # ✅ Ensure this matches "post/new/"
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # ✅ Ensure this matches "post/<int:pk>/update/"
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # ✅ Ensure this matches "post/<int:pk>/delete/"
]

