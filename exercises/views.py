from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import CustomUser

from .models import Exercises
from .serializers import ExerciseSerializer


class ExerciseCreateView(APIView):
    """Create a new Exercise"""

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = ExerciseSerializer

    def post(self, request, *args, **kwargs):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseListView(APIView):
    """List all Exercises | Administrators"""

    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (JWTAuthentication,)

    serializer_class = ExerciseSerializer

    def get(self, request, *args, **kwargs):
        exercises = Exercises.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExerciseDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = ExerciseSerializer

    """Get Exercises"""

    def get(self, request, *args, **kwargs):
        user_id = request.data["user"]

        exercises = Exercises.objects.filter(user=user_id)
        serializer = ExerciseSerializer(exercises, many=True)
        data = serializer.data
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "User Exercises",
            "data": data,
        }
        return Response(response, status=status.HTTP_200_OK)


class ExerciseUpdateView(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)

    serializer_class = ExerciseSerializer

    """Update an Exercise"""

    def put(self, request, pk):
        user_id = request.data.get("user")
        exercise = Exercises.objects.filter(user=user_id, id=pk).first()
        if not exercise:
            return Response(
                {"detail": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ExerciseSerializer(exercise, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "User Exercises",
                "data": data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDeleteView(APIView):
    """Delete an Exercise"""

    def delete(self, request, pk, *args, **kwargs):
        user_id = request.data.get("user")
        exercise = Exercises.objects.filter(user=user_id, id=pk).first()
        if not exercise:
            return Response(
                {"detail": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND
            )
        exercise.delete()
        response = {
            "status": "success",
            "code": status.HTTP_204_NO_CONTENT,
            "message": "Exercise deleted successfully",
        }
        return Response(response, status.HTTP_204_NO_CONTENT)
