from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Review

def home(request):
	context = {
		'page': 'Books',
		'books': Book.objects.all(),
	}
	return render(request, 'book/home.html', context)

class BookListView(ListView):
	model = Book
	template_name = 'book/home.html'
	context_object_name = 'books'
	ordering = ['title']
	#paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page'] = 'Books'
		context['css'] = 'book/main.css'
		return context


class BookDetailView(DetailView):
	model = Book
	template_name = 'book/detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page'] = 'Books'
		context['css'] = 'book/main.css'
		context['reviews'] = Review.objects.filter(book=self.kwargs['pk'])
		return context
