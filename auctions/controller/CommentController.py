from django.shortcuts import redirect, render

from auctions.forms.CommentForm import CommentForm
from auctions.models import CommentModel, AuctionModel


def add_comment(request, auction_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentModel()
            comment.title = form.cleaned_data['title']
            comment.comment = form.cleaned_data['comment']
            comment.auction = AuctionModel.objects.get(id=auction_id)
            comment.user = request.user

            comment.save()
            return redirect('listing', auction_id=auction_id)
        else:
            return redirect('index')

    else:
        return render(request, 'auctions/comment.html', {
            'auction': AuctionModel.objects.get(id=auction_id),
            'form': CommentForm()
        })