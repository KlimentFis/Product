from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from main.models import Product


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
        name = request.data.get('name', '')
        description = request.data.get('description', '')
        price = request.data.get('price', '')

        # Проверка на пустые поля и отрицательную цену
        if len(name) != 0 and len(description) != 0:
            try:
                if price >= 0:
                    serializer = ProductSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": "Цена не может быть отрицательной"}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({"error": "Неверный формат цены"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Имя и описание не могут быть пустыми"}, status=status.HTTP_400_BAD_REQUEST)