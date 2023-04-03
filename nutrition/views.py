from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer


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
