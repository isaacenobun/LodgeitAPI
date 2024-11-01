from rest_framework import serializers
from .models import Staff, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']

class StaffSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Staff
        fields = ['id', 'email', 'username', 'owner', 'notification', 'password', 'company', 'company_id']
        extra_kwargs = {'password': {'write_only': True}, 'company': {'required': False, 'allow_null': True}}
        
    def create(self, validated_data):
        user = Staff(
            email=validated_data['email'],
            username=validated_data['username'],
            owner=validated_data.get('owner', False),
            notification=validated_data.get('notification', True),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user