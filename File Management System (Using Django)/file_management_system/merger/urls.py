from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# router = routers.DefaultRouter()
# router.register(r'merge', views.MergeAndSave.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'merge', views.MergeAndSave.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)