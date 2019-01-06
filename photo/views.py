from django.shortcuts import render
from django.views.generic import ListView
from .models import Picture

def home(request):
	context = {
		'page': 'Photos',
		'pictures': Picture.objects.all()
	}
	return render(request, 'photo/home.html', context)

class PictureListView(ListView):
	model = Picture
	template_name = 'photo/home.html'
	context_object_name = 'pictures'
	ordering = ['title']
	paginate_by = 5