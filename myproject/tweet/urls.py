from django.urls import path
from .views import (
    tweet_list, tweet_create, tweet_edit, tweet_delete, login_view, CustomLogoutView
)

urlpatterns = [
    path('', tweet_list, name='tweet_list'),
    path('tweets/create/', tweet_create, name='tweet_create'),
    path('tweets/edit/<int:tweet_id>/', tweet_edit, name='tweet_edit'),
    path('tweets/delete/<int:tweet_id>/', tweet_delete, name='tweet_delete'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]


