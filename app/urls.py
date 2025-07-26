from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('book', views.book, name="book"),
    path('about', views.about, name="about"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('delete/<int:book_id>/', views.delete_p_details, name='delete_p_details'),
    path('approve/<int:patient_id>/', views.approve, name='approve'),
    path('approve_form/<int:patient_id>/', views.approve_form, name='approve_form'),
]
