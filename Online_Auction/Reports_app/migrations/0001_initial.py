# Generated by Django 4.0.5 on 2022-06-21 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessReport',
            fields=[
                ('success_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('max_amt_bid', models.BigIntegerField()),
                ('is_sold', models.BooleanField()),
                ('auctiondetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails')),
                ('product_buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='Auction_app.bidder')),
                ('product_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedbackText', models.TextField()),
                ('rating', models.BooleanField()),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CancelReport',
            fields=[
                ('cancel_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.CharField(max_length=300)),
                ('auctiondetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails')),
            ],
        ),
        migrations.CreateModel(
            name='AuctionQuery',
            fields=[
                ('auction_query_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_query', models.TextField()),
                ('auctiondetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails')),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
