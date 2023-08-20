from rest_framework import serializers
from .models import Books

class Serialized_books(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'