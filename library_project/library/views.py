from django.shortcuts import render
from rest_framework import generics, response
from user.models import User
from .models import Library, UserBook
from .serializers import LibrarySerializers

class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.filter(borrowed=False)
    serializer_class = LibrarySerializers

class LibraryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers

class BorrowBookView(generics.GenericAPIView):
    model = Library.objects.all()
    
    def post(self, request, pk):
        user_id = request.data.get("user_id")
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return response.Response({"error": "User does not exist."}, status=400)
        
        try:
          book = Library.objects.get(id=pk)
        except Library.DoesNotExist:
            return response.Response({"error": "Book does not exist."}, status=400)
      
        UserBook.objects.create(user=user, book=book)
        book.borrowed = True
        book.save(update_fields=["borrowed"])
 
        return response.Response({"message": "Book borrowed."})
