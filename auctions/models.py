from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cost(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='user_who_makes_the_cost')
    title = models.CharField(max_length=100)
    description = models.TextField()
    person = models.ForeignKey(
        'Person', on_delete=models.CASCADE, related_name='person_to_use', default=1)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='category_for_the_cost', default=3)
    Costs = models.CharField(max_length=140, default="0$")
    comments = models.ManyToManyField(
        'Comment', related_name='comments_in_the_cost', blank=True)
    bids = models.ManyToManyField(
        'Bid', related_name='bids_in_the_cost', blank=True)
    last_bid = models.ForeignKey('Bid', on_delete=models.CASCADE,
                                 related_name='last_bid_for_the_cost', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    receipt = models.ImageField(upload_to='images', blank=True, null=True)
    closed = models.BooleanField(default=False)

    def datepublished(self):
        return self.date.strftime('%B %d %Y')

    def __str__(self):
        return self.title


class Person(models.Model):
    person = models.CharField(max_length=60)
    category = models.ManyToManyField('Category', blank=True, null=True)

    def __str__(self):
        return self.person


class Bid(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='user_who_make_the_bid')
    auction = models.ForeignKey(
        'Auction', on_delete=models.CASCADE, related_name='auction_for_the_bid')
    bid = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % (self.bid)


class Comment(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='user_who_make_the_comment')
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.user, self.date)


class PersonalWatchlist(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='user_for_the_watchlist')
    auctions = models.ManyToManyField(
        'Auction', related_name='auctions_in_the_watchlist', blank=True)

    def __str__(self):
        return 'Personal watchlist for %s' % (self.user)
