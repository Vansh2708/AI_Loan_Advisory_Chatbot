from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'email',
            'password',
            'phone',
            'credit_score',
            'annual_income'
        ]
    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            credit_score=validated_data.get('credit_score',650),
            annual_income=validated_data.get('annual_income',0)
            
        )
        return user