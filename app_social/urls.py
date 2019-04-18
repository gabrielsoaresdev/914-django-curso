
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core.views import index, persons, add_person,edit_person,get_persons_json


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^persons/$', persons),
    url(r'^persons_json/$', get_persons_json),
    url(r'^persons/add/$', add_person),
    url(r'^persons/(?P<person_id>.*)/edit/$', edit_person),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registro/login.html'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
