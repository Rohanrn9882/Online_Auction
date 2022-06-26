from django.db import models
from Seller_app.models import ProductInformation
from User_app.models import MyUser

# Create your models here.
class AuctionDetails(models.Model):
    auction_details_id = models.AutoField(primary_key=True)
    product_information = models.ForeignKey(ProductInformation, on_delete=models.CASCADE)
    auction_details_date = models.DateField()
    auction_start_time = models.DateTimeField()
    auction_time_span = models.DurationField()

    def __str__(self):
        return str(self.auction_details_id)

class UserWishlist(models.Model):
    user_wishlist_id = models.AutoField(primary_key=True)
    auction_details = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    wishlisted = models.BooleanField()

    def __str__(self):
        return str(self.wishlisted)

class CurrentAuction(models.Model):
    current_auction_id = models.AutoField(primary_key=True)
    auction_details = models.OneToOneField(AuctionDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.auction_details)

class Bidder(models.Model):
    bidder_id = models.AutoField(primary_key=True)
    currentauction = models.ForeignKey(CurrentAuction, on_delete=models.CASCADE)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    bidder_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.bidder_type)

class AutoBid(models.Model):
    autobid_id = models.AutoField(primary_key=True)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    starting_price = models.BigIntegerField()
    increment_price_by = models.BigIntegerField()
    max_price = models.BigIntegerField()

    def __str__(self):
        return str(self.bidder)

class SecurityDeposite(models.Model):
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    deposit_amt = models.BigIntegerField()
    currentauction = models.ForeignKey(CurrentAuction, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.deposit_amt)

class CurrentBid(models.Model):
    current_bid_id = models.AutoField(primary_key=True)
    currentauction = models.ForeignKey(CurrentAuction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    current_bid_time = models.DateTimeField(auto_now=True)
    current_bid_amt = models.BigIntegerField()

    def __str__(self):
        return str(self.current_bid_amt)

class AllBid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    auctiondetails = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    bidder = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
    bid_amt = models.BigIntegerField()

    def __str__(self):
        return str(self.bid_amt)