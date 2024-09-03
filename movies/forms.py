from django import forms

class MovieSearchForm(forms.Form):
    query = forms.CharField(max_length=255, label='Search for a movie:')

