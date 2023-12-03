from django.urls import path
from . import views, signup_view, login_view, logout_view, profile_view

urlpatterns = [
    path('signup/', signup_view.signup, name='signup'),
    path('login/', login_view.login, name='login'),
    path('logout/', logout_view.logout, name='logout'),
    path('profile/', profile_view.profile, name='profile'),
]