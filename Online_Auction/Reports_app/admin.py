from django.contrib import admin
from .models import *

# Register your models here.
class SuccessReportAdmin(admin.ModelAdmin):
    list_display = ['success_report_id', 'auctiondetails', 'max_amt_bid', 'product_buyer', 'product_owner']
admin.site.register(SuccessReport, SuccessReportAdmin)

class CancelReportAdmin(admin.ModelAdmin):
    list_display = ['cancel_report_id', 'auctiondetails', 'reason']
admin.site.register(CancelReport, CancelReportAdmin)

class AuctonQueryAdmin(admin.ModelAdmin):
    list_display = ['auction_query_id', 'myuser', 'auctiondetails', 'user_query']
admin.site.register(AuctionQuery, AuctonQueryAdmin)

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['feedback_id', 'myuser', 'feedbackText', 'rating']
admin.site.register(FeedBack, FeedBackAdmin)