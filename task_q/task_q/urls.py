"""task_q URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from appmanager.views import login_form, login_check, sign_up, create_user, reset_user, reset_password, home, home_save_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_form),
    path('logincheck', login_check),
    path('signup/', sign_up),
    path('create_user', create_user),
    path('reset', reset_user),
    path('reset_password', reset_password),
    path('home/', home),
    path('home_save', home_save_data)
]
