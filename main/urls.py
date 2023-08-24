from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *


urlpatterns = [
    path('home/', PublicationsListView.as_view(), name='home'),
]
