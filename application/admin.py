from django.contrib import admin
from django.contrib.auth import get_user_model 
User=get_user_model()
from .models import *

class InscriptionAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj =None):
        return request.user.is_staff
    
    def has_delete_permission(self, request, obj =None):
        return request.user.is_staff
    
    def has_add_permission(self, request):
        return request.user.is_staff

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'matricule', 'code_formateur','code_parent')
    list_filter = ('role',)

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('user', 'option', 'niveau', 'date_inscription')
    search_fields = ('user_username', 'user_matricule')

@admin.register(Preinscription)
class PreinscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'option','niveau', 'statut')
    list_filter = ('nom','statut','option')
        

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    display = ('nom')
    search_fields = ['nom']
    
@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    display = ('nom')
    search_fields = ['nom']
    
    
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('nom','filiere')
    search_fields = ('nom','filiere')


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'coefficient', 'option')
    search_fields = ('nom',)
    list_filter = ('nom','option')

@admin.register(Enseignement)
class EnseignementAdmin(admin.ModelAdmin):
    list_display = ('formateur', 'matiere')
    search_fields = ('formateur',)
    list_filter = ('formateur','matiere')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'matiere', 'valeur')
    search_fields = ('etudiant',)
    list_filter = ('etudiant','matiere')
    
@admin.register(Emargement)
class EmargementAdmin(admin.ModelAdmin):
    list_display = ('formateur', 'date', 'heure_cours')
    search_fields = ('formateur','date')
    list_filter = ('formateur','date')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'titre', 'contenu','date_publication','approuve')
    search_fields = ('auteur','titre', 'contenu')
    list_filter = ('auteur','titre','contenu')

class DefaultAdmin(admin.ModelAdmin):
  pass