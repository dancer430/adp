from django.urls import path

from appointment import views


urlpatterns = [
    path('menu_html/', views.menu_html, name="menu_html"),
    path('appointment_html/', views.appointment_html, name="appointment_html"),
    path('appointment_list/', views.appointment_list, name="appointment_list"),
    path('appointment_operation/', views.appointment_operation, name="appointment_operation")
]