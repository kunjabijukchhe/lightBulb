from django.urls import path

from . import views

app_name = "lightApp"
urlpatterns = [

    path('', views.index,name='button'),
    path("logout/", views.logout_view, name="logout"),
    path("app/", views.dashboard, name="dashboard"),



]
