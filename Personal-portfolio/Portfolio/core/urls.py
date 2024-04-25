from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
     path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
      path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
