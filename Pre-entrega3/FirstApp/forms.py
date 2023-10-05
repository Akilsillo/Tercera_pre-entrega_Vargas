from django import forms

class GamesForm(forms.Form):
    name = forms.CharField()
    release_date = forms.CharField()
    rating = forms.FloatField()
    
class Projects(forms.Form):
    name = forms.CharField()
    approx_time = forms.CharField()
    description = forms.CharField()
    
class HobbiesForm(forms.Form):
    name = forms.CharField()
    
class SearchGame(forms.Form):
    name = forms.CharField()