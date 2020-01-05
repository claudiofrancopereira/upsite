# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

from django.views.generic.edit import FormView
#from .forms import FileFieldForm

from .models import Album
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
        
            return redirect( 'albums:list' )
    else:
        form = forms.CreateAlbum()


    return render( request, 'albums_create.html', {'form': form } )

def albums_detail( request, slug ):
    album = Album.objects.get( slug = slug )
    return render( request, 'albums_detail.html', {'album': album } )

# def albums_upload( request ):
# 	list = []

# 	if request.method == "POST":

# 		for f in request.FILES.getlist('files_to_be_upload'):
# 			filename = f.name
# 			list.append( filename )

# 		print( list )

# 	return render( request, 'albums_upload.html', {'files': list } )
# # Create your views here.

# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'albums_upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 instance = Image(image=file)  # match the model.
#                 instance.save()
#             return self.form_valid(form)
#         else:
#         	print( form )
#         	return self.form_invalid(form)
