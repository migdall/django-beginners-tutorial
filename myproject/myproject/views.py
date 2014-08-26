# Default application views

from django.shortcuts import render_to_response
from myproject.notes.models import Note

def hello( request ):
    notes = Note.objects.all()
    return render_to_response('index.html', {'notes': notes})
