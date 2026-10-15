

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Expense
from .serializers import ExpenseSerializer


def index(request):
    return render(request, 'expenses/index.html')


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer