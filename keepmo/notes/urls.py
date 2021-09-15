from django.urls import path
from .views import indexView, profileView, createNotebookView, notebookDetailView, createNoteView, exploreNoteBooksView, editNotebookView, editNoteView, exploreProfileView, registerView, editProfileView



urlpatterns = [
 	path('', indexView, name='index'),
 	path('profile/', profileView, name='profile'),
 	path('createNotebook/', createNotebookView, name='create_notebook'),
 	path('notebook/<int:id>', notebookDetailView, name='detailed_notebook'),
 	path('createNote/<int:id>', createNoteView, name='create_note'),
 	path('explore/', exploreNoteBooksView, name='explore'),
 	path('exploreProfile/<int:id>', exploreProfileView, name='explore_profile'),
 	path('notebookEdit/<int:id>', editNotebookView, name='edit_notebook'),
 	path('noteEdit/<int:id>', editNoteView, name='edit_note'),
 	path('register/', registerView, name='register'),
 	path('editProfile/', editProfileView, name='edit_profile'),
]