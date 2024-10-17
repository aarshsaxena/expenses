from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseCreateView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        # Additional logic for calculating splits can be added here
        serializer.save()

class ExpenseDetailView(generics.RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseListView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class DownloadBalanceSheetView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        # Logic to generate downloadable balance sheet
        return Response({"message": "Balance sheet functionality here."})
