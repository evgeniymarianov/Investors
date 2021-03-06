from django.urls import path, include
from . import views
from .views import DocumentView, PassportDetailView, PassportListView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('passport_file_upload/', PassportListView.as_view(), name='passport-upload'),
    path('passport_data_upload/<int:pk>/', PassportDetailView.as_view(), name='passport-data-upload'),
    path('qualification_status/<int:pk>/', views.QualificationStatusView.as_view(), name='set-qualification-status'),
    path('document_upload/', DocumentView.as_view(), name='document-upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
