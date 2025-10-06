from django.urls import path
from .views import LibraryListCreateView, LibraryDetailView, BorrowBookView

urlpatterns = [
    path("", LibraryListCreateView.as_view()),
    path("<int:pk>/", LibraryDetailView.as_view()),
    path("<int:pk>/borrow/", BorrowBookView.as_view()),
]

