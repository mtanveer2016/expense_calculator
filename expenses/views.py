

from rest_framework.viewsets import ModelViewSet  # pyright: ignore[reportMissingImports]

from .models import Expense
from .serializers import ExpenseSerializer  # pyright: ignore[reportMissingImports]


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer