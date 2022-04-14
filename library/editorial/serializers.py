from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EditorialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Editorial
		fields = [ 'id', 'name', 'address', 'country']


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = [ 'id', 'phone','name', 'address', 'country', 'employees_qnt', 'company_role']