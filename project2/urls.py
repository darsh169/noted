"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from accounts.views import Home,Regester,Login,DoRegister,DoLogin,DoLogout,Account
from accounts.views import SaveNote,ShowNote,Delete,Update
from django.contrib.auth.models import User,auth

import accounts

app_name='accounts'

urlpatterns = [
	path('',Home),
	path('register',Regester),
	path('do_register',DoRegister),
	path('do_login',DoLogin),
	path('account',Account),
	path('login',Login),
	path('logout',DoLogout),
	path('save_note/<int:user_id>',SaveNote),
	path('show_note',ShowNote,name='show_note'),
	path('delete/<int:note_id>',Delete),
	path('update/<int:note_id>',Update),
    path('admin/', admin.site.urls),
]
