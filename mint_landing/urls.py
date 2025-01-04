from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('about', views.about, name='news'),
    path('contact', views.contact, name='news'),
    path('vision-mission-values', views.v_m_s, name='vms'),
    path('organizational-structure', views.o_s, name='o_s'),
    path('power-duties', views.p_d, name='p_d'),
    path("get_translations", views.get_translations, name="get_translations")
]

