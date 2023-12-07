from django.urls import path

from .views import login_view, logout_view, sign_up

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', sign_up, name='sign_up'),
]