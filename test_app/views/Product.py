from rest_framework import viewsets, exceptions
from test_app.serializer import ProductSerializer
from test_app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer


@api_view(['GET'])
def products_by_category(request, categoryId):
    try:
        if categoryId:
            products = Product.objects.filter(category=categoryId)
            return Response(ProductSerializer(products, many=True).data)

    except Exception as e:
        return Response(data={'message': 'Error listando los productos de una categoria'
                                     + e.__str__(), 'data': None, 'code': 500})


@api_view(['GET'])
def relastets_product(request, productId):
    try:
        if productId:
            tags = Product.objects.get(pk=productId).tags.all()
            productList = Product.objects.filter(tags__in=tags).distinct().exclude(pk=productId).order_by('-created_at')[:5]
            return Response(ProductSerializer(productList, many=True).data)

    except Exception as e:
        return Response(data={'message': 'Error listando productos relacionados'
                                         + e.__str__(), 'data': None, 'code': 500})





