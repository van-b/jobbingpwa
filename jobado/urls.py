#-*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'jobado'

urlpatterns = [

	#path('categories/', views.CategoryView.as_view(), name = 'categories'),
	#path('update/<int:pk>', views.PosterUpdateView.as_view(), name='update_poster'),
	path('index/', views.index, name='index'),
	path('base_layout', views.base_layout, name='base_layout'),
	path('registration/', views.JobberCreateView.as_view(), name='registration'),
	path('signup/', views.PosterCreateView.as_view(), name='signup'),
	path('login/', views.UserLoginView.as_view(), name='login'),
	path('logout/', views.UserLogoutView.as_view(), name='logout'),
	path('personal/', views.personal, name='personal'),
	path('new_job/', views.new_job, name='new_job'),
	#path('services/<int:pk>/', views.DetailView.as_view(), name='detail'),
	#path('post/new/', views.post_new, name='post_new'),
	#path('delete/<int:pk>', views.PosterDeleteView.as_view(), name='delete_poster'),
]