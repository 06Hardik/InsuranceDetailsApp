from django.contrib import admin
from django.urls import path
from cust_insurance_app.views import get_policy_details_by_id, get_policy_count_for_month_by_region

urlpatterns = [
    path('get_policy_details_by_id', get_policy_details_by_id),
    path('get_policy_count_for_month_by_region', get_policy_count_for_month_by_region),
]