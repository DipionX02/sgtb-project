from django.forms import ModelForm # Importamos o ModelForm do django
from .models import * # Importamos o model

class CreatePassageiroForm(ModelForm):
	class Meta:
		model = Passageiro
		fields = ['nome','cpf','email'] 


class CreateMalaForm(ModelForm):
	class Mala:
		model = Mala
		fields = ['data','rfid','passageiro']