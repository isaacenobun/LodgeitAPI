from rest_framework import serializers
from .models import Staff, Company

from rest_framework.validators import UniqueValidator

import bleach

class CompanySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if (len(value) > 10):
            raise serializers.ValidationError('The name of your company is too long')
        return bleach.clean(value)
    class Meta:
        model = Company
        fields = ['id', 'name']

class StaffSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Staff.objects.all())])
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True,required=False)
    class Meta:
        model = Staff
        fields = ['id', 'email', 'username', 'owner', 'notification', 'password', 'company', 'company_id']
        extra_kwargs = {'password': {'write_only': True}, 'company': {'required': False, 'allow_null': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance