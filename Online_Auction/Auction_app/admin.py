from django.contrib import admin
from .models import *

# Register your models here.
class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ['auction_details_id', 'product_information', 'auction_details_date', 'auction_start_time', 'auction_time_span']
admin.site.register(AuctionDetails, AuctionDetailsAdmin)

class UserWishlistAdmin(admin.ModelAdmin):
    list_display = ['user_wishlist_id', 'auction_details', 'myuser', 'wishlisted']
admin.site.register(UserWishlist, UserWishlistAdmin)

class CurrentAuctionAdmin(admin.ModelAdmin):
    list_display = ['current_auction_id', 'auction_details']
admin.site.register(CurrentAuction, CurrentAuctionAdmin)

class BidderAdmin(admin.ModelAdmin):
    list_display = ['bidder_id', 'currentauction', 'myuser', 'bidder_type']
admin.site.register(Bidder, BidderAdmin)

class AutoBidAdmin(admin.ModelAdmin):
    list_display = ['autobid_id', 'bidder', 'starting_price', 'increment_price_by', 'max_price']
admin.site.register(AutoBid, AutoBidAdmin)

class SecurityDepositeAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'deposit_amt', 'currentauction']
admin.site.register(SecurityDeposite, SecurityDepositeAdmin)

class CurrentBidAdmin(admin.ModelAdmin):
    list_display = ['current_bid_id', 'currentauction', 'bidder', 'current_bid_time', 'current_bid_amt']
admin.site.register(CurrentBid, CurrentBidAdmin)

class AllBidAdmin(admin.ModelAdmin):
    list_display = ['bid_id', 'auctiondetails', 'bidder', 'bid_time', 'bid_amt']
admin.site.register(AllBid, AllBidAdmin)