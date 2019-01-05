from django.shortcuts import render

def home(request):
	context = {
	}
	return render(request, 'static/home.html', context)