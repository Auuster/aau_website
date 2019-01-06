from django.shortcuts import render

def home(request):
	context = {
		'css': 'static/main.css',
	}
	return render(request, 'static/home.html', context)