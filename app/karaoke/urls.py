from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^audio/', views.Record_Audio.as_view(), name='record_audio')
]