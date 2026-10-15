from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('expenses.urls')),   # brings in "/" and "/api/expenses/"
]

admin.site.site_header = "Expense Calculator"