from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """
    A view to contact the owner.
    """
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for your message!")
            return redirect("contact")
        messages.error(request, "Error: Please try again")
    template = "contact/contact.html"
    context = {
        "form": form,
    }
    return render(request, template, context)
