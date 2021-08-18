from django.db.models.query import QuerySet
from rest_framework import permissions
import trip
from django.contrib.auth.models import User
from trip.permissions import TripIsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from trip.models import Trip
from trip.serializers import TripCreateSerializer, TripListSerializer, TripDetailSerialzier, TripUpdateSerializer, TripUploadSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.views import APIView 
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser




class TripCreate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    permission_classes = ( TripIsOwnerOrReadOnly, )
    serializer_class = TripCreateSerializer
    


class TripList(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer
    permission_classes = ( AllowAny, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'trip_title', 'city', 'state,' ]
    

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    permission_classes = ( TripIsOwnerOrReadOnly, )
    serializer_class = TripDetailSerialzier
    


class TripDelete(DestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripCreateSerializer
    permission_classes = ( TripIsOwnerOrReadOnly, )

class TripUpdate(RetrieveUpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripUpdateSerializer
    permission_classes =  ( TripIsOwnerOrReadOnly, )

class TripUploadView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [FileUploadParser]
    
    def post(self, request, *args, **kwargs):
        trip = get_object_or_404(Trip.objects.all(), pk=self.kwargs['pk'])
        if "file" in request.data:
            file=request.data["file"]
            trip.c_photo.save(file.name, file, save=True)

        serializer = TripUploadSerializer(trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)