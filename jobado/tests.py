#-*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.shortcuts import redirect
from . import views

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djobbing.settings")

class PostersTest(TestCase):
	
	#fixtures = ['jobado_dataset.json']
	def test_login(self):
		"""
		Affichage de la page personnel d'un poster
		"""
		c = Client()
		response = c.post('/login/', {'username': 'john', 'password': 'smith'})
		self.assertEqual(response.status_code, 200)
'''
from django.db import models
from jobado.models import *

# Création d'un attribut
product_attribute = ProductAttribute(name="couleur")
product_attribute.save()

# Création des valeurs des attributs
attribute1 = ProductAttributeValue(value="bleu", product_attribute=product_attribute, position=0)
attribute1.save()

attribute2 = ProductAttributeValue(value="jaune", product_attribute=product_attribute, position=0)
attribute2.save()

attribute2 = ProductAttributeValue(value="brun", product_attribute=product_attribute, position=0)
attribute2.save()

# Création du produit
product = Product(name="Tshirt", code="54065", price_ht=25, price_ttc=30)
product.save()

# Création d'une déclinaison de produit
product_item = ProductItem(product=product, code="5046", code_ean13="a1")
product_item.save()
product_item.attributes.add(attribute1)
product_item.attributes.add(attribute1)
product_item.save()
'''