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

    def validate(self, data):
        if data['splitMethod'] == 'percentage':
            # Add logic to validate that percentages add up to 100%
            pass
        return data
