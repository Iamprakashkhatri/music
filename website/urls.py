from django.contrib import admin
from django.conf.urls import url,include
app_name='music'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
]
