#-*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustumUser, Category, Service, City, District, Jobber, Poster, Job, Application, Attachment

class CustumUserAdmin(UserAdmin):
	class Meta:
		model = CustumUser

class CategoryAdmin(admin.ModelAdmin):
	empty_value_display = ''
	#inlines = [ServiceInline]
	list_display = ('id','name', 'description')

	class Meta:
		model = Category

class ServiceAdmin(admin.ModelAdmin):
	empty_value_display = ''
	list_display = ('id','name', 'description')

	class Meta:
		model = Service

class CityAdmin(admin.ModelAdmin):
	empty_value_display = ''
	list_display = ('id','name')

	class Meta:
		model = City

class DistrictAdmin(admin.ModelAdmin):
	empty_value_display = ''
	list_display = ('id','name')

	class Meta:
		model = District

class JobberAdmin(admin.ModelAdmin):
	empty_value_display = ''
	fieldsets = [('Informations du compte', {'fields': ['district', 'sex', 'username', 'last_name', 'first_name', 'email', 'phone_number', 'photo', 'password', 'is_active']}), ('Informations du profil jobber', {'fields': ['biography', 'categories']}),]
	list_display = ('username','district', 'sex', 'last_name', 'first_name', 'email', 'phone_number', 'biography', 'note',)
	

	class Meta:
		model = Jobber

class PosterAdmin(admin.ModelAdmin):
	empty_value_display = ''
	fieldsets = [('Informations du compte', {'fields': ['district', 'sex', 'username', 'last_name', 'first_name', 'email', 'phone_number', 'photo', 'password', 'is_active']}),]
	list_display = ('username','district', 'sex', 'last_name', 'first_name', 'email', 'phone_number')

	class Meta:
		model = Poster

class JobAdmin(admin.ModelAdmin):
	empty_value_display = ''

	class Meta:
		model = Job

class ApplicationAdmin(admin.ModelAdmin):
	empty_value_display = ''

	class Meta:
		model = Application

class AttachmentAdmin(admin.ModelAdmin):
	empty_value_display = ''
	list_display = ('id','application_id', 'content')

	class Meta:
		model = Attachment

admin.site.unregister(Group)
admin.site.register(CustumUser,CustumUserAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Jobber, JobberAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Application,ApplicationAdmin)
admin.site.register(Attachment,AttachmentAdmin)
