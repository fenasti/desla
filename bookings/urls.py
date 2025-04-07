from . import views
from django.urls import path

urlpatterns = [
    path('', views.reservation_page, name='reservation'),
    path('edit_reservation/<int:reservation_id>', views.edit_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>', views.delete_reservation, name='delete_reservation'),
]
