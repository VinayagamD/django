from django.urls import re_path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name="list"),
    re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name="detail"),
    re_path(r'^create/$', views.SchoolCreateView.as_view(), name="create"),
    re_path(r'update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name="update"),
    re_path(r'delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name="delete"),
]
