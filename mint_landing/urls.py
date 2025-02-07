from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news", views.news, name="news"),
    path(
        "announcement/<int:id>", views.announcement_detail, name="announcement_detail"
    ),
    path(
        "load-more-announcements/",
        views.load_more_announcements,
        name="load_more_announcements",
    ),
    path("about", views.about, name="about"),
    path("request-support", views.contact, name="contact"),
    path(
        "submit-support-request",
        views.submit_support_request,
        name="submit_support_request",
    ),
    path("support-request-success", views.success_view, name="success_view"),
    path("vision-mission-values", views.v_m_s, name="vms"),
    path("organizational-structure", views.o_s, name="o_s"),
    path("power-duties", views.p_d, name="p_d"),
    path("get_translations", views.get_translations, name="get_translations"),
    path("components/<int:id>", views.component_detail, name="component_detail"),
    path(
        "pdf-resources/download/<int:id>/",
        views.resource_download,
        name="resource_download",
    ),
    path("team", views.team_members, name="team_members"),
    path("resources", views.resources, name="resources"),
    # Auth
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
