from django.contrib import admin
from .models import*

# Register your models here.
#admin.site.register(Courses)

@admin.register(Eleve)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom','genre', 'status','serie')
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Personnel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom','prenom','genre', 'grade',)
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Adresse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email', 'quartier', 'ville',)
    ordering = ('email',)
    search_fields = ('email',)
    
@admin.register(Etablissement)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricule','nom','arrete','date','logo')
    ordering = ('nom',)
    search_fields = ('nom',)

@admin.register(Matiere)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'coefficient','note', 'appreciation', )
    ordering = ('nom', )
    search_fields = ('nom', )