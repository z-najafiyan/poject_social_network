"""socialnetwork URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from apps.account import views
from apps.account.views import CompleteProfile
from socialnetwork import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('user/', include('apps.account.urls')),
    path('post/', include('apps.post.urls')),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
    path('', TemplateView.as_view(template_name='index.html'), name="home"),
    path('ok/', TemplateView.as_view(template_name='ok.html'), name="ok"),
    path('complete_edit/<int:pk>/', CompleteProfile.as_view(), name='complete_profile'),
    path(r'^password/$', views.change_password, name='change_password'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
