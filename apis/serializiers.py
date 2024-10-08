from rest_framework import serializers
from .models import Banks,Branches

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model=Banks
        fields='__all__'


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model=Branches
        fields='__all__'
        depth = 1