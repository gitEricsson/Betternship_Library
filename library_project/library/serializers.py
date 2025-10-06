from rest_framework import serializers
from .models import Library

class LibrarySerializers(serializers.ModelSerializer):
  class meta:
    model = Library
    fields = ["id", "title", "author" "published_date"]