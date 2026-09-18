from django.urls import path
from .views import (
    registration_list,
    register_event,
    user_registrations,
    cancel_registration
)

urlpatterns = [
    path('', registration_list, name='registration-list'),
    path('register/', register_event, name='register-event'),
    path('user/<int:user_id>/', user_registrations, name='user-registrations'),
    path('<int:registration_id>/cancel/', cancel_registration, name='cancel-registration'),
]


