import calendar
import datetime

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from exercises.models import Exercises
from workout.models import Workout
from workout.serializers import WorkoutSerializer


class WorkoutPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class WorkoutCreateView(APIView):
    """Create a new Workout"""

    serializer_class = WorkoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutListView(APIView):
    """List all Workout | Administrators"""

    # permission_classes = (IsAuthenticated, IsAdminUser)
    # authentication_classes = (JWTAuthentication,)

    serializer_class = WorkoutSerializer

    def get(self, request, *args, **kwargs):
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkoutDetailView(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)
    pagination_class = WorkoutPagination

    serializer_class = WorkoutSerializer

    """Get workout"""

    def get(self, request, *args, **kwargs):
        user_id = request.data["user"]
        workouts = Workout.objects.filter(user=user_id)

        # Filter by date
        date = request.query_params.get("date", None)
        if date:
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
            workouts = workouts.filter(date=date)

        page = self.pagination_class()
        page_data = page.paginate_queryset(workouts, request)
        serializer = self.serializer_class(page_data, many=True)
        response = page.get_paginated_response(serializer.data)
        data = response.data
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "User workouts",
            "data": data,
        }
        return Response(response, status=status.HTTP_200_OK)


class WorkoutUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    serializer_class = WorkoutSerializer

    """Update an workout"""

    def put(self, request, pk):
        user_id = request.data.get("user")
        workout = Workout.objects.filter(user=user_id, id=pk).first()
        if not workout:
            return Response(
                {"detail": "Workout not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = WorkoutSerializer(workout, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "User Workout Updated Successfully",
                "data": data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDeleteView(APIView):
    """Delete an workout"""

    def delete(self, request, pk, *args, **kwargs):
        user_id = request.data.get("user")
        workout = Workout.objects.filter(user=user_id, id=pk).first()
        if not workout:
            return Response(
                {"detail": "workout not found"}, status=status.HTTP_404_NOT_FOUND
            )
        workout.delete()
        response = {
            "status": "success",
            "code": status.HTTP_204_NO_CONTENT,
            "message": "Workout deleted successfully",
        }
        return Response(response, status.HTTP_204_NO_CONTENT)
