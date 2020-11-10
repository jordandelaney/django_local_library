from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Book list page
    path('books/', views.BookListView.as_view(), name='books'),

    #Book detail view
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # Authors list view
    path('authors/', views.AuthorListView.as_view(), name='authors'),

    # Author detail view
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # Loaned books list view
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    # All books for librarians
    path('borrowed/', views.AllLoanedBooksListView.as_view(), name='all-borrowed'),

    # Librarian renew book instance due date
    path('book/<uuid:pk>/renew', views.renew_book_librarian, name='renew-book-librarian'),

    # Create Author 
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),

    # Update Author
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),

    # Delete author
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),

    # Create a book
    path('book/create/', views.BookCreate.as_view(), name='book_create'),

    # Update a book
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),

    # Delete book
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]