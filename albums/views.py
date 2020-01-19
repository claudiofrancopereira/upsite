# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, AlbumImages
from . import forms


def albums_list( request ):
    albums = Album.objects.all()
    return render( request, 'albums_list.html', { 'albums': albums } )

@login_required( login_url='/accounts/login/')
def albums_create( request ):
    if request.method == 'POST':
        form = forms.CreateAlbum( request.POST )
        
        if form.is_valid():
            instance = form.save( commit = False )
            instance.author = request.user
            instance.save()

            for f in request.FILES.getlist( 'files' ):
                image = AlbumImages( album = Album.objects.get( title = instance.title ), image = f, posted = instance.author )
                image.save()

            return redirect( 'albums:list' )
    else:
        form = forms.CreateAlbum()


    return render( request, 'albums_create.html', {'form': form } )

def albums_detail( request, slug ):
    album = Album.objects.get( slug = slug )
    images = AlbumImages.objects.filter( album = album )

    return render( request, 'albums_detail.html', {'album': album, 'images': images } )

# def albums_upload( request ):
# 	list = []

# 	if request.method == "POST":

# 		for f in request.FILES.getlist('files_to_be_upload'):
# 			filename = f.name
# 			list.append( filename )

# 		print( list )

