from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Album( models.Model ):
	title = models.CharField( max_length = 100 )
	description = models.TextField( null = True, blank = True )
	author = models.ForeignKey( User, default = None, on_delete = models.CASCADE )
	slug = models.SlugField( unique = 100 )
	date = models.DateTimeField( auto_now_add = True )

	class Meta:
		unique_together = ( 'title', 'slug' )

	def __str__( self ):
		return self.title 

	def get_absolute_url( self ):
		return reverse( "albums:detail", kwargs = { "slug": self.slug } )

class AlbumImages( models.Model ):
    album = models.ForeignKey( Album, on_delete = models.CASCADE )
    image = models.ImageField( upload_to = 'albums/images' )
    posted = models.ForeignKey( User, default = None, on_delete = models.CASCADE )
    
    def __unicode__( self ):
    	return self.album.title
