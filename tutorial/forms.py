from tkinter import Widget
from django import forms
from .models import Cataory,Coures,Tutoris,Bodycors


class Cataoryform(forms.ModelForm):
    class Meta:
        model=Cataory
        fields=('name',)
        Widget = {
                  'name':forms.TextInput(attrs={'class':'form-control'})
            }
class CouresForm(forms.ModelForm):
    class Meta:
        model=Coures
        fields=('cours_name','img','catagory')
        Widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'img':forms.ImageField(),
            'catagory':forms.Select(attrs={'class':'form-control'}),
        }


class TutorisForm(forms.ModelForm):
    class Meta:
        model=Tutoris
        fields=('cours','titel',)
        Widget = {
            'cours':forms.Select(attrs={'class':'form-control'}),
            'titel':forms.TextInput(attrs={'class':'form-control'}),
        }

class BodycorsForms(forms.ModelForm):
    class Meta:
        model=Bodycors
        fields=('select_cours','select_titel','body')
        Widget = {
            'select_cours':forms.Select(attrs={'class':'form-control'}),
            'select_titel':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateCataoryform(forms.ModelForm):
    class Meta:
        model=Cataory
        fields=('name',)
        Widget = {
                  'name':forms.TextInput(attrs={'class':'form-control'})
            }