from re import template
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView,RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('api/',include('api.urls')),
]
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('api.urls')),
    re_path('', RedirectView.as_view(url='/')),
]
"""