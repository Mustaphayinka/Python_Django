
# Function based view path
# Function based view path
# Function based view path


# from django.contrib import admin
# from django.urls import path, include
# from booksapi.views import book_list, book_create, book

# urlpatterns = [
#     path('',book_create),
#     path('list/',book_list),
#     path('<int:pk>', book)
#     ]


# Class based view path
# Class based view path
# Class based view path

from django.urls import path, include
from booksapi.views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view()),
    ]