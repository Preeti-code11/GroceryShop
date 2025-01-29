from django.urls import path
from .views import notifications_list, mark_as_read

urlpatterns = [
    path('', notifications_list, name='notifications_list'),
    path('mark_as_read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]
