from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import NoteBook, Note, Profile
from .forms import NoteBookForm, NoteForm, NewUserForm, EditProfileForm
from django.contrib.auth import login
from datetime import datetime

# Create your views here.
def indexView(request):
	return render(request, 'index.html')

login_required(login_url='login')
def profileView(request):
	context = {'notebooks': NoteBook.objects.filter(owner=request.user.profile)}
	return render(request, 'profile.html', context)

@login_required(login_url='login')
def createNotebookView(request):
	if request.method == "POST":
		form = NoteBookForm(request.POST, {'owner':request.user.profile})
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('profile'))
	form = NoteBookForm({'owner':request.user.profile})
	return render(request, 'createNotebook.html', {'form': form})

def notebookDetailView(request, id):
	notebook = get_object_or_404(NoteBook, id=id)
	try:
		notes = Note.objects.filter(notebook_id=id)
	except Note.DoesNotExist:
		return HttpResponseRedirect(reverse('create_note', kwargs={'id':id}))
	return render(request, 'notebook.html', {'notebook':notebook, 'notes':notes})

def createNoteView(request, id):
	notebook = get_object_or_404(NoteBook, id=id)
	if request.method == 'POST':
		form = NoteForm(request.POST, {'created_at': datetime.now(), 'notebook':notebook})
		if form.is_valid():
			form.save()
			return notebook.get_absolute_url()
	form = NoteForm({'created_at': datetime.now(), 'notebook':notebook})
	return render(request, 'create_note.html', {'form':form})


def exploreNoteBooksView(request):
	notebooks = get_list_or_404(NoteBook, is_public=True)
	return render(request, 'explore_notes.html', {'notebooks':notebooks})

def editNotebookView(request, id):
	notebook = get_object_or_404(NoteBook, id=id)
	if request.method == "POST":
		form = NoteBookForm(request.POST, instance=notebook)
		if form.is_valid():
			form.save()
			return notebook.get_absolute_url()
	form = NoteBookForm(instance=notebook)
	return render(request, 'edit_notebook.html', {'form':form})

def editNoteView(request, id):
	note = get_object_or_404(Note, id=id)
	if request.method == "POST":
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return note.notebook.get_absolute_url()
	form = NoteForm(instance=note)
	return render(request, 'edit_note.html', {'form':form})

def exploreProfileView(request, id):
	profile = get_object_or_404(Profile, id=id)
	notebooks = get_list_or_404(NoteBook, owner=profile, is_public=True)
	return render(request, 'explore_profile.html', {'profile':profile, 'notebooks':notebooks})

def registerView(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("index")
	form = NewUserForm()
	return render (request, "registration/register.html", {"register_form":form})

@login_required(login_url="login")
def editProfileView(request):
	profile = request.user.profile
	if request.method == "POST":
		form = EditProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
	form = EditProfileForm(instance=profile)
	return render(request, 'edit_profile.html', {'form':form})