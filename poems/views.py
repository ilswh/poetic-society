from django.shortcuts import render
from .models import Poem, Comment

# Create your views here.

def view_poems(request):
    poems = Poem.objects.all()
    template = "poems/poems.html"
    context = {
        "poems": poems,
    }
    return render(request, template, context)

def view_comments(request):
    comments = poem.comments.all().order_by("-created_on")
    comment_count = poem.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.poem = poem
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()

    return render(request,
        {
            "poem": poem,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )


def edit_comment(request, comment_id):
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
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('poem_detail'))


def delete_comment(request, comment_id):
    queryset = Post.objects.filter(status=1)
    poem = get_object_or_404(queryset)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('poem_detail'))
