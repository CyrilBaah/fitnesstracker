from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    """Health check view"""

    def get(self, request, *args, **kwargs):
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "Backend lunched successfully",
            "version": "0.1.0",
        }
        return Response(response, status.HTTP_503_SERVICE_UNAVAILABLE)
