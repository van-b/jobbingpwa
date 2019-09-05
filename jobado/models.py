#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import Permission, AbstractUser, Group 
from phonenumber_field.modelfields import PhoneNumberField
#from django.core.mail import send_mail

def update_last_login(sender, user, **kwargs):
	"""
	A signal receiver which updates the last_login date for
	the user logging in.
	"""
	user.last_login = timezone.now()
	user.save(update_fields=['last_login'])


class City(models.Model):
	
	name = models.CharField(verbose_name = 'nom', max_length = 50, null = False, blank = False)
	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Villes'
		verbose_name = 'Ville'
		ordering = ['-id']

class District(models.Model):
	city = models.ForeignKey(City, related_name = 'districts', on_delete = models.CASCADE)
	name = models.CharField(verbose_name = 'nom', max_length = 50, null = False, blank = False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Quartier'
		verbose_name_plural = 'Quartiers'

class CustumUser(AbstractUser):

	F = 'femme'
	M = 'homme'
	SEXE_CHOICES = [

	    (F, 'F'),
	    (M, 'M'),

	]

	username_validator = UnicodeUsernameValidator()
	district = models.ForeignKey(District, on_delete = models.CASCADE, related_name = 'particuliers', verbose_name = 'quartier',default=1)
	sex = models.CharField(max_length = 5, choices = SEXE_CHOICES, default = M, verbose_name = 'sexe')
	last_name = models.CharField(blank=False, max_length=150, verbose_name='nom(s)', )
	first_name = models.CharField(blank=False, max_length=30, verbose_name='prenom(s)')
	username = models.CharField(error_messages={'unique': 'Un utilisateur avec ce pseudo existe deja.'}, help_text='Obligatoire,seulement des lettres, chiffres et @/./+/-/_ ', max_length=150, unique=True, validators=[username_validator], verbose_name='pseudo')
	email = models.EmailField(blank=False, max_length=254, verbose_name='adresse email')
	password = models.CharField(max_length=128, verbose_name='mot de passe', help_text = 'donner un mot de passe fort')
	phone_number = PhoneNumberField(unique = True, verbose_name = 'numéro de téléphone')
	photo = models.ImageField(upload_to = 'profile_images/', verbose_name = 'image de profil')
	date_joined = models.DateTimeField(default=timezone.now, verbose_name='date inscription')
	is_active = models.BooleanField(default=True, help_text="designe si l'utilisateur a le droit de se connecter au site", verbose_name='actif')
	last_login = models.DateTimeField(blank=True, null=True,)
	is_superuser = models.BooleanField(default=False,)
	is_staff = models.BooleanField(default=False,)
	groups = models.ManyToManyField(Group,verbose_name='groups',blank=True,help_text='un utilisateur appartenant a ce groupe aura les autorisations associees',related_name="groupes_utilisateur",related_query_name="utilisateur",)
	user_permissions = models.ManyToManyField(Permission, blank=True, help_text='autorisations specifiques pour cet utilisateur.', related_name='permissions', verbose_name="permissions_de_l'utilisateur")

	class Meta(AbstractUser.Meta):
		abstract =False

class Poster(CustumUser):
	class Meta:
		verbose_name = 'Poster'
		verbose_name_plural = 'Posters'
		ordering = ['-id']


class Category(models.Model):

    name = models.CharField(max_length = 50, null = False, verbose_name = 'nom')
    description = models.TextField(verbose_name = 'description', default ='ensemble de services a la personnes (SAP)')
    

    def __str__(self):
        return self.name

    class Meta:
    	
    	verbose_name = 'Categorie'
    	verbose_name_plural = 'Categories'
    	ordering = ['-id']

class Service(models.Model):
    category = models.ForeignKey(Category, related_name = 'services', on_delete = models.CASCADE, verbose_name = 'categorie')
    name = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'nom')
    description = models.TextField(null = True, verbose_name = 'description')

    def __str__(self):
    	return self.name

class Job(models.Model):
	poster = models.ForeignKey(Poster, related_name = 'needs', on_delete = models.CASCADE)
	service = models.ForeignKey(Service, related_name = 'jobs', on_delete = models.CASCADE,)
	description = models.TextField()
	completion_date = models.DateField(verbose_name = 'date de réalisation')
	completion_hour = models.TimeField(verbose_name = 'heure de réalisation')
	expiration_date = models.DateField(verbose_name = "date d'expiration")
	jobbers_number = models.PositiveIntegerField(default = 1, verbose_name = 'nombre nécessaire de jobbers')
	unit_price = models.PositiveIntegerField(verbose_name = 'remunération par jobber')
	#lorqu'on poste un job il est soit pret soit en attente
	state = models.BooleanField(default = False, verbose_name = 'état')
	#un job est soit non realise/0, soit semi-realise/1 soit realise/2
	realised = models.PositiveIntegerField(default = 0, verbose_name = 'réalisé')
	pub_date = models.DateField(auto_now_add = True, verbose_name = 'date de publication')
	

	def __str__(self):
		return self.service.name

	class Meta:
		verbose_name = 'Job'
		ordering = ['-pub_date']

class Jobber(Poster):
	categories = models.ManyToManyField(Category, related_name = 'jobbers', db_table = 'category_jobber')
	biography = models.TextField(verbose_name = 'mini biographie')
	note = models.FloatField(default = 0)

	class Meta:
		verbose_name = 'Jobber'
		ordering = ['-id']

class Application(models.Model):
	jobber = models.ForeignKey(Jobber, on_delete = models.CASCADE, related_name = 'applications',)
	need = models.ForeignKey(Job, related_name = 'postulations', on_delete = models.CASCADE, verbose_name = 'job')
	terms_of_service = models.TextField(verbose_name = 'modalités de prestation')
	#une candidature peut etre voté/True ou pas/False
	status = models.BooleanField(default = False, verbose_name ='voté')
	evaluation = models.FloatField(verbose_name = 'évaluation')
	

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Candidature'
		verbose_name_plural = 'Candidatures'

class Attachment(models.Model):
	application = models.ForeignKey(Application, on_delete = models.CASCADE, related_name = 'attachments', verbose_name = 'candidature')
	content = models.FileField(upload_to = 'attachments/', verbose_name = 'contenu')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'pièce jointe'
		verbose_name_plural = 'pièces jointes'

