from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Poem
from .forms import PoemForm


def view_poems(request):
    """
    A view to list all poems.
    """
    poems = Poem.objects.all()
    template = "poems/poems.html"
    context = {
        "poems": poems,
    }
    return render(request, template, context)


def view_poem(request, poem_id):
    """
    A view to display a poem.
    """
    poem = get_object_or_404(Poem, id=poem_id)
    template = "poems/poem.html"
    context = {
        "poem": poem,
    }
    return render(request, template, context)


def add_poem(request):
    """
    A view to add a new poem via the front-end.
    """
    form = PoemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            new_poem = form.save()
            messages.success(request, "Poem added!")
            return redirect(view_poem, poem_id=new_poem.pk)
        messages.error(request, "Error: Please try again")
    template = "poems/add_poem.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


def edit_poem(request, poem_id):
    """
    A view to edit an existing poem via the front-end.
    """
    poem = get_object_or_404(Poem, id=poem_id)
    if request.user != poem.author:
        messages.error(request, "Access denied. Please try again")
        return redirect(view_poem, poem_id=poem_id)
    form = PoemForm(request.POST or None, instance=poem)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Poem Updated!")
            return redirect(view_poem, poem_id=poem_id)
        messages.error(request, "Error: Please try again")
    template = "poems/edit_poem.html"
    context = {
        "poem": poem,
        "form": form,
    }
    return render(request, template, context)


def delete_poem(request, poem_id):
    """
    A view to delete an existing poem via the front-end.
    """
    poem = get_object_or_404(Poem, id=poem_id)
    if request.user != poem.author:
        messages.error(request, "Access denied. Please try again")
        return redirect(view_poem, poem_id=poem_id)
    poem.delete()
    messages.success(request, "Poem deleted.")
    return redirect("poems")
