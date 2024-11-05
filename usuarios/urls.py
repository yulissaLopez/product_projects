from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.UserList.as_view(), name = 'user_list'),
    path('<int:pk>', views.UserDetail.as_view(), name = 'user_detail'),


    path("sign-up/", views.SignUp.as_view(), name='sign_up'),
    path("login/", views.Login.as_view(), name = "login"),
    path("my_profile/", views.Profile.as_view(), name='my-profile'),

    # Authentication
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

