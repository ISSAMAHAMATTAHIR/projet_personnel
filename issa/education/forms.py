from django import forms
from django.forms import ModelForm
from .models import Eleve, Adresse, Etablissement


class EleveForm(forms.ModelForm):
	class Meta:
		model = Eleve
		fields = ['matricule','nom', 'prenom', 'naissance', 'lieu','genre', 'nationalite','photo',]

		labels = {
			'matricule': 'Matricule', 
			'nom': 'Nom',  
			'Prenom' : 'Prenom',     
			'naissance' : 'date de naissance ',
			'lieu' : 'lieu de naissance ',
			'genre' : 'genre',
			'nationalite ' : 'Nationalite ',
			'photo': 'Selectionner une photo',
			  
		}

		widgets = {
			'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le matricule',}), 
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}), 
			'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}), 
			'naissance': forms.TextInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'lieu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lieu de naissance',}), 
			'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre',}), 
			'nationalite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationalite',}),   
			'adresse': forms.Select(attrs={'class': 'form-select', 'placeholder': 'adresse',}),
			#'photo': forms.ImageField()
		}

# class AdresseForm(forms.ModelForm):
# 	class Meta:
# 		model = Adresse
# 		fields = [ 'telephone', 'email', 'quartier', 'ville',]

# 		labels = {
# 			'telephone': 'Telephone',
# 			'email': 'Email',
# 			'quartier': 'Quartier ',
# 			'ville': 'Ville',
# 		}

# 		widgets = {
# 			'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le numéro',}),
# 			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Saisir l\'email', }),
# 			'quartier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le quartier', }),
# 			'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir la ville', }),
# 		}


# class EtablissementForm(forms.ModelForm):
# 	class Meta:
# 		model = Etablissement
# 		fields = [ 'nom', 'montant', 'validation',]

# 		labels = {
# 			'nom': 'Nom',
# 			'montant': 'Montant',
# 			'validation': 'Validation ',
# 		}

# 		widgets = {
# 			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'veillez saisir le nom de la banque',}),
# 			'montant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le montant', }),
# 			'validation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'La validation', }),
# 		}


# class RecuForm(forms.ModelForm):
# 	class Meta:
# 		model = Recu
# 		fields = [ 'date', 'montant', 'reste', 'numero', 'employe', ]

# 		labels = {
# 			'date': 'Date',
# 			'montant': 'Montant',
# 			'reste': 'Reste ',
# 			'numero': 'Numero ',
# 			'employe': 'employe ',
# 		}

# 		widgets = {
# 			'date': forms.TextInput(attrs={'class': 'form-control','type':'datetime-local'}),
# 			'montant': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le montant', }),
# 			'reste': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le reste', }),
# 			'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Le numero', }),
# 			'employe': forms.Select(attrs={'class': 'form-control', 'placeholder': 'L\'employé', }),


# 		}


