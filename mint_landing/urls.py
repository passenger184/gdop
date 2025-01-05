from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('announcement/<int:id>',
         views.announcement_detail, name='announcement_detail'),
    path('about', views.about, name='about'),
    path('request-support', views.contact, name='contact'),
    path('submit-support-request', views.submit_support_request,
         name='submit_support_request'),
    path('support-request-success', views.success_view, name='success_view'),
    path('vision-mission-values', views.v_m_s, name='vms'),
    path('organizational-structure', views.o_s, name='o_s'),
    path('power-duties', views.p_d, name='p_d'),
    path("get_translations", views.get_translations, name="get_translations")
]
