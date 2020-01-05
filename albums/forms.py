from django import forms
from . import models

class CreateAlbum( forms.ModelForm ):
	class Meta:
		model = models.Album
		fields = [ 'title', 'description']