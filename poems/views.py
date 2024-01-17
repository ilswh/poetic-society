from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .models import Poem, Comment
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

def view_comments(request):
    """
    A view to display comments.
    """
    comments = poem.comments.all().order_by("-created_on")
    comment_count = poem.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.poem = poem
            comment.save()
            messages.success(
                request, 'Comment submitted and awaiting approval'
            )
    comment_form = CommentForm()

    template = "poems/comments.html"
    context = {
        "poem": poem,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form
    }
    return render(request, template, context)


def edit_comment(request, comment_id):
    """
    A view to edit a comment.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.poem = poem
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return render(reverse('poem_detail'))


def delete_comment(request, comment_id):
    """
    A view to delete a comment.
    """
    queryset = Post.objects.filter(status=1)
    poem = get_object_or_404(queryset)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return render(reverse('poem_detail'))
