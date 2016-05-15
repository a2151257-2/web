"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from qa import views as qa_views

urlpatterns = [
    url(r'^$', qa_views.nf, name='home'),
    url(r'^login/$', qa_views.nf, name='login'),
    url(r'^signup/$', qa_views.nf, name='signup'),
    url(r'^question/[^ /]+/$', qa_views.test, name='question'),
    url(r'^ask/$', qa_views.nf, name='ask'),
    url(r'^popular/$', qa_views.nf, name='popular'),
    url(r'^new/$', qa_views.nf, name='new'),
    url(r'^admin/', admin.site.urls)
    #url(r'^', include('qa.urls'))
]