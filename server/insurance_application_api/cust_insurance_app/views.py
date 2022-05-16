from email import policy
from cust_insurance_app.serializers import CustomerDetailsSerializer, PolicyDetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from cust_insurance_app.models import CustomerDetails, PolicyDetails
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

@api_view(('GET',))
def get_policy_details_by_id(request, *args, **kwargs):
    search_id = request.GET.get('id')
    id_type = request.GET.get('type')
    if (id_type == "Policy"):
        policy_detail = PolicyDetails.objects.filter(PolicyId = search_id)
        customer_details = policy_detail.get().CustId
    else:
        customer_details = CustomerDetails.objects.get(CustId=search_id)
        policy_detail = customer_details.policydetails_set.all()
    
    serializer = PolicyDetailsSerializer(policy_detail, many=True)
    cust_serializer = CustomerDetailsSerializer(customer_details, many=False)
    return Response({"policy_details":serializer.data, "customer_Details": cust_serializer.data},status=status.HTTP_200_OK)

@api_view(('GET',))
def get_policy_count_for_month_by_region(request, *args, **kwargs):
    region = request.GET.get('region')
    policyDetails = PolicyDetails.objects.filter(CustId__Region=region)
    serializer = PolicyDetailsSerializer(policyDetails, many=True)

    somevar = policyDetails.annotate(month=TruncMonth('Purchase_date')).values('month').annotate(policyCount=Count('PolicyId')).values('month', 'policyCount').order_by('month')
    serialized_q = json.dumps(list(somevar), cls=DjangoJSONEncoder)

    return Response(serialized_q, status=status.HTTP_200_OK)

@api_view(('POST',))
def update_policy_details(request, *args, **kwargs):
    policy_details = request.data.get('policy_details')
    policy_details_obj = PolicyDetails.objects.get(PolicyId=policy_details['PolicyId'])
    policy_details_obj.Premium = policy_details['Premium']
    policy_details_obj.Fuel = policy_details['Fuel']
    policy_details_obj.VEHICLE_SEGMENT = policy_details['VEHICLE_SEGMENT']
    policy_details_obj.Bodily_Injury_Liability = policy_details['Bodily_Injury_Liability']
    policy_details_obj.Collision = policy_details['Collision']
    policy_details_obj.Comprehensive = policy_details['Comprehensive']
    policy_details_obj.Personal_Injury_Protection = policy_details['Personal_Injury_Protection']
    policy_details_obj.Property_Damage_Liability = policy_details['Property_Damage_Liability']
    policy_details_obj.save()
    return Response("updated", status=status.HTTP_200_OK)
