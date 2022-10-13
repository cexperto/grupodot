"""grupodot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from customUser.models import CustomUser
from customUser.userViews import CustomUserList, AllUsers
from findpalindromos import views
from findpalindromos.views import Palindrome


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='customUser.urls'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    
    path('user/<int:pk>/', CustomUserList.as_view()),
    path('api/auth/', include(('customUser.urls','customUser'))),
    path('allUsers/', AllUsers.as_view()),#just get all with out authentication
    path('palindrome', Palindrome.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)