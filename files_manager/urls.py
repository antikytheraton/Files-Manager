from files.views import FileViewSet
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from django.contrib import admin

router = SimpleRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
