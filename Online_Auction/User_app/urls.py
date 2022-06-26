from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name = 'register_url'),
    path('login/', views.LoginView.as_view(), name = 'login_url'),
    path('logout/', views.LogoutView.as_view(), name = 'logout_url'),
    path('otp/', views.OTPView.as_view(), name = 'otp_url'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(), name='activate_url'),
    path('home/', views.HomeView.as_view(), name = 'home_url'),

    path('showuser/<int:id>/', views.showUserView, name='show_url'),
    path('updatprofile/<int:id>/', views.updateProfileView, name='update_url'),
    path('deactivate/<int:id>/', views.deleteProfileView, name='delete_url')

]