from django.urls import path
from .views import *


urlpatterns = [
    path('', BloglistView, name='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('review/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
]