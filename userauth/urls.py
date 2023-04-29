from django.urls import path
from userauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('editprofile/', views.editProfile, name='editprofile'),

    path('sign-up/', views.register, name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out')
]
