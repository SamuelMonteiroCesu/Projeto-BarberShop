from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from BarberShop.views import *
from BarberShop import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Status Procedure Payment Company Employee Client 

router = routers.DefaultRouter()
router.register(r'status', StatusViewSet)
router.register(r'procedure', ProcedureViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'client', ClientViewSet)
router.register(r'bugbounty', BugBountyViewSet)
router.register(r'schedule', ScheduleViewSet)
router.register(r'appointment', AppointmentViewSet)
router.register(r'dayoff', DayOffViewSet)
#router.register(r'prof', UserViewSet)


urlpatterns = [
    
    path('test/',views.home),
    path('getuser/',views.GetUserViewSet),
    path('getprof/',views.GetProfViewSet),
    path('passrecover/',views.PassRecoverViewSet),
    path('passchange/',views.PassChangeViewSet),
    path('freeschedule/',views.FreescheduleViewSet),
    path('myschedule/',views.MyScheduleViewSet),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view(),
    )



]
