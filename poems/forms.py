from django import forms
from .models import Poem


class PoemForm(forms.ModelForm):
    """
    Form to allow managine Poems.
    """
    class Meta:
        model = Poem
        fields = "__all__"
        exclude = ("author",)
