"""Senufo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Senufo_App import views
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/admin', permanent=False)), # temp redirect to admin
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^Map_Print/$', views.map_working, name="Create CSV"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^NetworkEdgesAcquiredFrom/', views.NetworkEdgesAcquiredFrom, name="NetworkEdgesAcquiredFrom"),
    url(r'^NetworkEdgesCreatorCollector/', views.NetworkEdgesCreatorCollector, name="NetworkEdgesCreatorCollector"),
    url(r'^Map_Print_DrawingPhoto/$', views.map_working_drawingphoto, name="Create CSV 2"),
    url(r'^Map_Print_Collection/$', views.map_working_collection, name="Create CSV 3"),
    url(r'^MappedWork_Page/$', views.mapped_work_webpage_view, name="Mapped Work Page"),
    url(r'^exportworks_latlong/$', views.exportworks_latlong, name="Works with LatLong"),
    url(r'^exportworks_latlong_prov/$', views.exportworks_latlong_prov, name="Works with LatLong and Provenance"),
    url(r'^links/$', views.links, name="links"), 
    url(r'^exportworksplaces_latlong/$', views.exportworksplaces_latlong, name="WorkPlaces with LatLong"),
#    url(r'^Page/$', views.Page, name="Page"),
]
