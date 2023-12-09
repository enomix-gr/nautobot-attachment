# urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<pk>/delete/', views.AttachmentDeleteView.as_view(), name='attachment_delete'),
    path('add-to/location/<pk>/', views.AttachmentAddView.as_view(), name='attachment_add'),
]
