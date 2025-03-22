from django.contrib import admin
from movie.models import Pelicula

from django import forms
# Register your models here.

# admin.site.register(Pelicula)

class PeliculaAdminForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'generos': forms.SelectMultiple,
        }

class PeliculaAdmin(admin.ModelAdmin):
    form = PeliculaAdminForm

admin.site.register(Pelicula, PeliculaAdmin)
