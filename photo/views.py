from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture

def home(request):
	context = {
		'page': 'Photos',
		'pictures': Picture.objects.all()
	}
	return render(request, 'photo/home.html', context)