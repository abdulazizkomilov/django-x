from django.urls import path
from app import views
from django.contrib.auth.views import LogoutView

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
]

hmtx_views = [
    path("check-username/", views.check_username, name='check-username'),
]

urlpatterns += hmtx_views
