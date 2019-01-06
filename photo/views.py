from django.shortcuts import render
from django.views.generic import ListView
from .models import Picture

def home(request):
	context = {
		'css': 'photo/main.css',
		'page': 'Photos',
		'pictures': Picture.objects.all(),
	}
	return render(request, 'photo/home.html', context)

class PictureListView(ListView):
	model = Picture
	template_name = 'photo/home.html'
	context_object_name = 'pictures'
	ordering = ['title']
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['page'] = 'Photos'
		context['css'] = 'photo/main.css'
		return context