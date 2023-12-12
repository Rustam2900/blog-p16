from django.urls import path

from .views import login_view, logout_view, sign_up, user_profile, change_password, user_profile_edit

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', sign_up, name='sign_up'),
    path('profile/', user_profile, name='user_profile'),
    path('password-change/', change_password, name='change_password'),
    path('profile-update/', user_profile_edit, name='user_profile_edit'),
]