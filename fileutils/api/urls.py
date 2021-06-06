from django.urls import path
from fileutils.api.views import ApiUploadsListView, api_upload_files_view

app_name='dathesense'

urlpatterns = [
    path('list/',ApiUploadsListView.as_view(),name='list'),
    path('upload',api_upload_files_view,name='upload'),
]