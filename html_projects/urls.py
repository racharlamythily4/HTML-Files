"""
URL configuration for html_projects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("table1/",table1,name='table1'),
    path("table2/",table2,name='table2'),
    path("table3/",table3,name='table3'),
    path("ass4/",ass4,name='ass4'),
    path("ass5/",ass5,name='ass5'),
    path("form1/",form1,name='form1'),
    path("form2/",form2,name='form2'),
    path("form3/",form3,name='form3'),
    path("transform/",transform,name='transform'),
    path("ass6/",ass6,name='ass6'),
    path("ass7/",ass7,name='ass7'),
    path("facebook/",facebook,name='facebook'),
    path('keyframes/',keyframes,name='keyframes'),
    path('semantic/',semantic,name='semantic'),
    path('bs_local_model/',bs_local_model,name='bs_local_model'),
    path('bs_local_modal_navbar/',bs_local_modal_navbar,name='bs_local_modal_navbar'),
    path('cards/',cards,name='cards'),
    path('fancycards/',fancycards,name='fancycards'),
    path('horizantolcards/',horizantolcards,name='horizantolcards'),
    path('modals/',modals,name='modals'),
    path('navbar/',navbar,name='navbar')

]
