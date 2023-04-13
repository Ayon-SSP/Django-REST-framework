from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
# Create your views here.
@api_view(['GET'])
def getData(request):
#     person = {
#     "count": 2,
#     "next": None,
#     "previous": None,
#     "results": [
#         {
#             "email": "admin@example.com",
#             "groups": [],
#             "url": "http://localhost:8000/users/1/",
#             "username": "paul"
#         },
#     ]
# }
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)