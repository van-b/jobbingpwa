#-*- coding: utf-8 -*-
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
#from django.template import loader
#from django.http import Http404

from .models import *
from .forms import *


class PosterCreateView(generic.CreateView):
	template_name = 'inscriptions/signup.html'
	form_class = CustomUserCreationForm
	model = Poster
	success_message = 'Succes : votre compte a ete cree, veuilez vous connecter.'
	success_url = '/jobado/index'

def personal(request):
	jobber = get_object_or_404(Jobber, username=request.user.username)
	print(jobber.categories)
	return render (request, 'jobado/personal.html')

class UserLoginView(LoginView):

	form_class = UserAuthenticationForm
	template_name = 'inscriptions/login.html'
	redirect_authenticated_user = False


class UserLogoutView(LogoutView):
    template_name = 'jobado/index.html'
	

def index(request):
	jobs = Job.objects.all()
	posters = Poster.objects.all()
	categories = Category.objects.all()
	return render(request, 'jobado/index.html', {'jobs': jobs,'categories': categories, 'posters': posters})

def base_layout(request):
	return render(request, 'jobado/base.html')

def getdata(request):
	results = Job.objects.all()
	jsondata = serializers.serialize('json',results)
	return HttpResponse(jsondata)


class JobberCreateView(generic.CreateView):
	template_name = 'inscriptions/registration.html'
	form_class = JobberCreationForm
	model = Jobber
	success_message = 'Succes : votre compte a ete cree, veuillez vous connecter.'
	success_url = ('/jobado/index')

def new_job(request):
	if request.method == "POST":
		job_form = JobForm(request.POST)
		if job_form.is_valid:
			job = job_form.save(commit=False)
			job.poster = get_object_or_404(Poster, username=request.user.username)
			job.state = False
			job.realised = 0
			job.pub_date = timezone.now()
			job.save()
			return redirect('/jobado/')
	else:
		job_form = JobForm()
	return render(request, 'demandes/new_job.html', {'job_form': job_form})

"""
class CategoryView(generic.ListView):
	template_name = 'jobado/includes/nav.html'
	context_object_name = 'category_list'

	def get_queryset(self):

		return Category.objects.all()

class PosterUpdateView(BSModalUpdateView):
	model = Poster
	template_name = 'jobado/update_poster.html'
	form_class = PosterForm
	success_message = 'Succes: votre compte poster a bien ete mis a jour.'
	success_url = reverse_lazy('index')

class PosterDeleteView(BSModalDeleteView):
	model = Poster
	template_name = 'jobado/delete_book.html'
	success_message = 'Succes: votre compte poster a bien ete supprime.'
	success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
	form_class = CustomUserCreationForm
	template_name = 'jobado/signup.html'
	success_message = 'Succes: compte cree, vous pouvez a present vous connecter.'
	success_url = reverse_lazy('index')

class CustomLoginView(BSModalLoginView):
	authentication_form = CustomAuthenticationForm
	template_name = 'jobado/login.html'
	success_message = 'Succes: bienvenu dans votre espace personnel.'
	success_url = reverse_lazy('index')

class PosterFirstView(generic.CreateView):
	form_class = RegistrationForm
	model = Poster
	template_name = 'jobado/registration.html'
	success_url = '/jobado/personal/'

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			job = form.save(commit=False)
			job.poster = request.user
			job.state = False
			job.realised = 0
			job.pub_date = timezone.now()
			job.save()
			return redirect('job_detail', pk=job.pk)
	else:
		form = PostForm()
	return render(request, 'jobado/registration.html', {'form': form})


class FAQView(generic.TemplateView):
	template_name = 'jobado/faq.html'

class IndexView(generic.ListView):

	# normalement on devrait avoir jobado/service_list.html et la vue sera ServiceView
	template_name = 'jobado/index.html'
	context_object_name = 'service_list'
	paginate_by = 5

	def get_queryset(self):

		return Service.objects.all()


class DetailView(generic.DetailView):

	model = Service
	template_name = 'jobado/detail.html'
"""
