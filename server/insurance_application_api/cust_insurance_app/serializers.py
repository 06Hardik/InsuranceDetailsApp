from rest_framework import serializers
from .models import CustomerDetails, PolicyDetails
class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ["CustId", "Gender", "Income_Group", "Region", "Marital_status"]

class PolicyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyDetails
        fields = ["PolicyId", "CustId", "Purchase_date", "Fuel", "VEHICLE_SEGMENT", "Premium", "Bodily_Injury_Liability", "Personal_Injury_Protection", "Property_Damage_Liability", "Collision", "Comprehensive"]