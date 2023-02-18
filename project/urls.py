"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from crcikblogs import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('addblog/',views.AddblogPage,name='addblog'),
    path('addmeme/',views.AddmemePage,name='addmeme'),
    path('memes/',views.MemesPage,name='memes'),
    path('profile/',views.ProfilePage,name='profile'),
    path('saveurl/',views.saveurl,name='saveurl'),
    path('myblogs/',views.myblogs,name='myblogs'),
    path('mymemes/',views.mymemes,name='mymemes'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)