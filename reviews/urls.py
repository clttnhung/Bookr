from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include
from . import views
from .views import book_search
from rest_framework.routers import DefaultRouter
from . import views, api_views
router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)
urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path('book-search/', book_search, name='book_search'),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path("books/<int:book_pk>/reviews/new/", views.review_edit, name="review_create"),
    path(
        "books/<int:book_pk>/reviews/<int:review_pk>/",
        views.review_edit,
        name="review_edit",
    ),
    path('books/<int:pk>/media/', views.book_media, name='book_media'),
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(),name='login'),
]
