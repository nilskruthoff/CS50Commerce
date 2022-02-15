from auctions.models import Auction, Comment


def get_comments(auction: Auction) -> list:
    return auction.comment_set.all()


def add_comment(request, form, comment: Comment, auction: Auction):
    try:
        comment.title = form.cleaned_data['title']
        comment.comment = form.cleaned_data['comment']
        comment.auction = auction
        comment.user = request.user
        comment.save()
        return True
    except ValueError:
        return False
