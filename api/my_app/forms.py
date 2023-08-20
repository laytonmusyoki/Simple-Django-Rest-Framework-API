from .models import Books
from django import forms

class Add_book(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'

        widgets={
            "name":forms.TextInput(attrs={"placeholder":"Enter the name of the book"}),
            "author":forms.TextInput(attrs={"placeholder":"Enter author of the book"}),
            "year_published":forms.TextInput(attrs={"placeholder":"Enter year published"})
        }