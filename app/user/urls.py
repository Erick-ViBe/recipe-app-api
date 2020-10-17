from django.urls import path
from user import views as UserViews


app_name = 'user'

urlpatterns = [
    path(
        'create/',
        UserViews.CreateUserAPIView.as_view(),
        name='create'
    ),

    path(
        'token/',
        UserViews.CreateTokenAPIView.as_view(),
        name='token'
    ),

    path(
        'me/',
        UserViews.ManageUserAPIView.as_view(),
        name='me'
    ),
]
