from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

def home(request):
	context = {
		'page': 'Books',
		'books': Book.objects.all()
	}
	return render(request, 'book/home.html', context)

class BookListView(ListView):
	model = Book
	template_name = 'book/home.html'
	context_object_name = 'books'
	ordering = ['title']
	paginate_by = 5
