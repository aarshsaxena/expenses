from rest_framework import serializers
from .models import User, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'description', 'totalAmount', 'payer', 'participants', 'splitMethod', 'createdAt']
