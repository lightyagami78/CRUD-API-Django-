from django.shortcuts import render
from .models import Report

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import ReportSerializer


# For fetching all the data and Display
@api_view(['GET'])
def index(request):
    showall = Report.objects.all();
    serialreport = ReportSerializer(showall, many=True)
    return Response(serialreport.data)

# For fetching single data and display
@api_view(['GET'])
def productView(request, pk):
    product = Report.objects.get(id=pk)
    serialreport = ReportSerializer(product, many=False)
    return Response(serialreport.data)


# For ADD products in the list 
@api_view(['POST'])
def productAdd(request):
    serialdata = ReportSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)


# For updating the product
@api_view(['POST'])
def productUpdate(request,pk):
    product = Report.objects.get(id=pk)
    serialsreport = ReportSerializer(instance=product, data=request.data)

    if serialsreport.is_valid():
        serialsreport.save()

    return Response(serialsreport.data)


# For delete the product
@api_view(['GET'])
def productDelete(request,pk):
    product = Report.objects.get(id=pk)
    product.delete()
    showall = Report.objects.all();
    serialreport = ReportSerializer(showall, many=True)
    return Response(serialreport.data)



