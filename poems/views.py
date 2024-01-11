from django.shortcuts import render
from .models import Poem

# Create your views here.

def view_poems(request):
    poems = Poem.objects.all()
    template = "poems/poems.html"
    context = {
        "poems": poems,
    }
    return render(request, template, context)
