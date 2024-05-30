from django.shortcuts import render
from .models import Book

def home(request): 
    books = Book.objects.all() 
    context = {
        'books': books     
}
    return render(request, 'home.html', context=context)

def about(request):
    return render(request, 'about.html')



# Create your views here.
def books(request):
    books_list = [
        {
        'title' : 'Book1',
        'price': 100,
        'publication_year':1999,
        },
        {
        'title' : 'Book2',
        'price': 100,
        'publication_year':1999,
        },
        {
        'title' : 'Book3',
        'price': 100,
        'publication_year':1999,
        }                                  
        
    ]
    context = {
        'books': books_list,
   }