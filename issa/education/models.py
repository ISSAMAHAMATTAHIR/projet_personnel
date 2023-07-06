from django.db import models

class Personne(models.Model):
    Genre = (
        ('Masculin',('Masculin')),
        ('Feminin',('Feminin')),
    )
    nom = models.CharField(max_length = 200)
    prenom = models.CharField(max_length = 100)
    naissance = models.DateTimeField('date de naissance')
    lieu = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 32, choices = Genre)
    nationnalite = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to='static/photo', blank=True)

    def __str__(self):
        return self.nom

class Adresse(models.Model):
    telephone = models.CharField(max_length = 20, blank = True, unique = True)
    email = models.CharField(max_length = 250, unique = True)
    quartier = models.CharField(max_length = 200)
    ville = models.CharField(max_length = 200)

    def __str__(self):
        return self.email

class Matiere(models.Model):
    nom = models.CharField(max_length = 150)
    coefficient = models.FloatField(max_length = 15)
    note = models.FloatField(max_length = 15)
    appreciation = models.CharField(max_length = 150)

    def __str__(self):
        return self.nom
    
class Etablissement(models.Model):
    matricule = models.CharField(max_length = 150)
    nom = models.CharField(max_length = 150)
    arrete = models.CharField(max_length = 150)
    date = models.CharField(max_length = 150)
    logo = models.ImageField(upload_to='static/logo', blank=True)

    def __str__(self):
        return self.nom

class Eleve(Personne):
    Status = (
        ('Ancien', ('Ancien')),
        ('Nouveau', ('Nouveau')),
    )
    
    Serie = (
        ('Litteraire', ('Litterature')),
        ('Scientifique', ('Scince')),
        ('Technique commerçial', ('Technique Commerçial')),
        ('Technique Industrielle', ('Technique Industrielle')),
    )
    
    Niveau = (
        ('6 eme', ('6 eme')),
        ('5 eme', ('5 eme')),
        ('4 eme', ('4 eme')),
        ('3 eme', ('3 eme')),
        ('Second', ('Second')),
        ('premiere', ('premiere')),
        ('terminal', ('terminale')),    
    )
    matricule = models.CharField(max_length = 32, unique=True)
    status = models.CharField(max_length = 32, choices = Status)
    niveau = models.CharField(max_length = 32, choices = Niveau)
    serie = models.CharField(max_length = 32, choices = Serie)
    adresse = models.ForeignKey(Adresse, on_delete = models.CASCADE)
    Matiere = models.ManyToManyField(Matiere)

    def __str__(self):
        return self.matricule

class Personnel(Personne):
    matricule = models.CharField(max_length = 32)
    grade = models.CharField(max_length = 100)
    poste = models.CharField(max_length = 100)
    adresse = models.ForeignKey(Adresse, on_delete = models.CASCADE)
    matiere = models.ManyToManyField(Matiere)

    def __str__(self):
        return self.matricule