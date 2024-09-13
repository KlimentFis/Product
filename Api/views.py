from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from main.models import Product
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def all_products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')

        if name.len() == 0 or description == 0 or price < 0:
            return