from django.conf.urls import url

from .views import IndexView, ChooseTestView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^test/$', ChooseTestView.as_view(), name='choose_test'),
    url(r'^help/$', TemplateView.as_view(template_name='testownik/help.html'), name='help'),
]