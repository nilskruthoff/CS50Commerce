from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from auctions.forms.CommentForm import CommentForm
from auctions.models import Comment, Auction


@login_required
def add_comment(request, auction_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.title = form.cleaned_data['title']
            comment.comment = form.cleaned_data['comment']
            comment.auction = Auction.objects.get(id=auction_id)
            comment.user = request.user

            comment.save()
            return redirect('show_auction', auction_id=auction_id)
        else:
            return redirect('index')

    else:
        return render(request, 'auctions/forms/comment.html', {
            'auction': Auction.objects.get(id=auction_id),
            'form': CommentForm()
        })