from django.contrib import admin
from .models import NoteBook, Note, Profile

# Register your models here.
admin.site.register(NoteBook)
admin.site.register(Note)
admin.site.register(Profile)