from django.db import models
from Auction_app.models import Bidder
from User_app.models import MyUser
from Auction_app.models import AuctionDetails

# Create your models here.
class SuccessReport(models.Model):
    success_report_id = models.AutoField(primary_key=True)
    auctiondetails = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    max_amt_bid = models.BigIntegerField()
    product_buyer = models.ForeignKey(Bidder, on_delete=models.CASCADE, related_name='buyer')
    product_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='seller')
    is_sold = models.BooleanField()

    def __str__(self):
        return str(self.max_amt_bid)

class CancelReport(models.Model):
    cancel_report_id = models.AutoField(primary_key=True)
    auctiondetails = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    reason = models.CharField(max_length=300)

    def __str__(self):
        return str(self.cancel_report_id)

class AuctionQuery(models.Model):
    auction_query_id = models.AutoField(primary_key=True)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    auctiondetails = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    user_query = models.TextField()

    def __str__(self):
        return str(self.user_query)

class FeedBack(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    feedbackText = models.TextField()
    rating = models.BooleanField()

    def __str__(self):
        return str(self.myuser)