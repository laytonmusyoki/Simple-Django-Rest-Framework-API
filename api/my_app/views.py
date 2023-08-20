from django.shortcuts import render
from .serializer import Serialized_books
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .forms import Add_book

@api_view(['GET'])
def get_routes(request):
    routes=[
        {
            'Endpoint':'/books/',
            'method':'GET',
            'body':'None',
            'description':'Returns array of books'
        },
        {
            'Endpoint':'/books/get_book/id/',
            'method':'GET',
            'body':'None',
            'description':'Returns single books'
        },
        {
            'Endpoint':'/books/add_book/',
            'method':'POST',
            'body':{
                'name':'...',
                'author':'...',
                'year_published':'...'
            },
            'description':'adds one book'
        },
        {
            'Endpoint':'/books/update_book/id/',
            'method':'POST',
            'body':{
                'name':'...',
                'author':'...',
                'year_published':'...'
            },
            'description':'adds one book'
        },
        {
            'Endpoint':'/books/delete_book/id/',
            'method':'DELETE',
            'body':'None',
            'description':'Deletes a single book'
        }
        
    ]
    return Response(routes)

@api_view(['GET'])
def books(request):
    books=Books.objects.all()
    serializer=Serialized_books(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request,pk):
    books=Books.objects.get(id=pk)
    serializer=Serialized_books(books,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    serializer=Serialized_books(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_book(request,pk):
    book=Books.objects.get(id=pk)
    serializer=Serialized_books(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_book(request,pk):
    book=Books.objects.get(id=pk)
    book.delete()
    return Response("Book was deleted successfully")

def postdata(request):
    form=Add_book
    context={
        "form":form
    }
    return render(request,'data.html',context)