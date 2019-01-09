from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Profile

class ProfileDetailView(DetailView):
	model = Profile
	template_name= 'users/detail.html'

	def get_context_data(self, **kwargs):
			context=super().get_context_data(**kwargs)
			context['page'] = User.objects.filter(profile=self.kwargs['pk']).first().username
			context['css'] = 'users/main.css'
			context['user'] = User.objects.filter(profile=self.kwargs['pk']).first()
			return context


