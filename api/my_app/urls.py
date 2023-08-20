from django.urls import path
from .views import books,add_book,get_book,update_book,delete_book,postdata,get_routes

urlpatterns=[
    path('',get_routes,name='get_routes'),
    path('books/',books,name='books'),
    path('books/get_book/<str:pk>/',get_book,name='get_book'),
    path('books/add_book/',add_book,name='add_book'),
    path('books/update_book/<str:pk>/',update_book,name='update_book'),
    path('books/delete_book/<str:pk>/',delete_book,name='delete_book'),
    path('post/',postdata,name='postdata')
]
