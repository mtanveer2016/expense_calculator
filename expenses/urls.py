from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ExpenseViewSet, index


router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', index, name='index'),              # the HTML page at /
    path('api/', include(router.urls)),         # the API at /api/expenses/
]