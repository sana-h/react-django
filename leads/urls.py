from rest_framework import routers
from rest_framework import urlpatterns
from .api import LeadViewset

router= routers.DefaultRouter()
router.register('api/leads', LeadViewset,'leads')
urlpatterns=router.urls