from django.db import models
from User_app.models import MyUser
from Auction_app.models import AuctionDetails

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    auctiondetails = models.ForeignKey(AuctionDetails, on_delete=models.CASCADE)
    payment_status = models.BooleanField()
    payment_from = models.CharField(max_length=100)
    payment_to = models.CharField(max_length=100)
    payment_amt = models.BigIntegerField()

    def __str__(self):
        return str(self.payment_amt)