from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('email/', views.send_mail, name='index'),
    path("api/v4/send-mail/reset-password", views.resetPassword, name="resetPassword"),
]
