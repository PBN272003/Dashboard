from .models import User
from.serializer import UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.
def dash_data(request):
    data = User.objects.all()
    serializer = UserSerializer(data,many = True)
    return JsonResponse(serializer.data,safe=False)

class dashView(APIView):
    def get(self,request,format=None):
        data = User.objects.all()
        serializer = UserSerializer(data,many = True)
        return Response(serializer.data)
    
def get(self, request, format=None):
    queryset = User.objects.all()


    year = request.query_params.get('year')
    if year is not None:
        queryset = queryset.filter(year=year)
        serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)

def dashboard(request):
    return render(request, 'Dash/index.html')
