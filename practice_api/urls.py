from django.urls import path, include
from practice_api.views import  CompanyViewSet, EmployeeViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls) )
]
