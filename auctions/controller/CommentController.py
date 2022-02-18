from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from auctions.forms.CommentForm import CommentForm
from auctions.models import Comment
from auctions.services import AuctionsService, CommentService


@login_required
def add_comment(request, auction_id):
    auction = AuctionsService.get_auction(id=auction_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            CommentService.add_comment(request, form=form, comment=comment, auction=auction)
            return redirect('show_auction', auction_id)
        else:
            return redirect('show_auction', auction_id)
    else:
        return render(request, 'auctions/forms/comment.html', {
            'auction': auction,
            'form': CommentForm()
        })
