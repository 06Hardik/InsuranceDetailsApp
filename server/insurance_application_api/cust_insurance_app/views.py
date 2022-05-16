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
