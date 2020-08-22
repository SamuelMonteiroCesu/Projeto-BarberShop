from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BarberShop.views import StatusViewSet, ProcedureViewSet

router = routers.DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'procedure', ProcedureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
