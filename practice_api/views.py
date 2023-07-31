from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from practice_api.models import Company, Employee
from practice_api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):

        try:

            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)

            emps_serializer = EmployeeSerializer(employees, many=True, context={'request':request})
        
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': "Company does not exist"
            })


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
