from rest_framework.views import APIView
from .serializers import CartItemSerializer
from .models import CartItem
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        item = CartItem.objects.all()
        serializer = CartItemSerializer(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        srializer = CartItemSerializer(item, data=request.data, partial=True)
        if srializer.is_valid():
            srializer.save()
            return Response({"status": "success", "data": srializer.data})
        else:
            return Response({"status": "error", "data": srializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


