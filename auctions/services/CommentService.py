from datetime import datetime

from auctions.models import Auction, Comment
from auctions.services import BidService


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


def get_all_comments(auction: Auction):
    comments = auction.comment_set.all()
    for comment in comments:
        comment.date = get_date_time(comment.date)
    return comments


def get_date_time(date: datetime):
    return date.strftime('%d.%m.%Y %H:%M')
