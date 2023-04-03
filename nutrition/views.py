from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer


class NutritionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class NutritionCreateView(APIView):
    """Create a new Nutrition"""

    serializer_class = NutritionSerializer

    def post(self, request, *args, **kwargs):
        serializer = NutritionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutritionListView(APIView):
    """List all Nutrition | Administrators"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    serializer_class = NutritionSerializer

    def get(self, request, *args, **kwargs):
        nutrition = Nutrition.objects.all()
        serializer = NutritionSerializer(nutrition, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NutritionDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    pagination_class = NutritionPagination

    serializer_class = NutritionSerializer

    """Get nutritions"""

    def get(self, request, *args, **kwargs):
        user_id = request.data["user"]
        nutritions = Nutrition.objects.filter(user=user_id)
        page = self.pagination_class()
        page_data = page.paginate_queryset(nutritions, request)
        serializer = self.serializer_class(page_data, many=True)
        response = page.get_paginated_response(serializer.data)
        data = response.data
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "User nutritions",
            "data": data,
        }
        return Response(response, status=status.HTTP_200_OK)


class NutritionUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = NutritionSerializer

    """Update an nutrition"""

    def put(self, request, pk):
        user_id = request.data.get("user")
        nutrition = Nutrition.objects.filter(user=user_id, id=pk).first()
        if not nutrition:
            return Response(
                {"detail": "Nutrition not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = NutritionSerializer(nutrition, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "User Nutrition Updated Successfully",
                "data": data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NutritionDeleteView(APIView):
    """Delete an nutrition"""

    def delete(self, request, pk, *args, **kwargs):
        user_id = request.data.get("user")
        nutrition = Nutrition.objects.filter(user=user_id, id=pk).first()
        if not nutrition:
            return Response(
                {"detail": "nutrition not found"}, status=status.HTTP_404_NOT_FOUND
            )
        nutrition.delete()
        response = {
            "status": "success",
            "code": status.HTTP_204_NO_CONTENT,
            "message": "Nutrition deleted successfully",
        }
        return Response(response, status.HTTP_204_NO_CONTENT)
