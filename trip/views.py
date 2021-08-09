from trip.permissions import TripIsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from trip.models import Trip
from trip.serializers import TripCreateSerializer, TripListSerializer, TripDetailSerialzier
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated



class TripCreate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = TripCreateSerializer



class TripList(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer
    permission_classes = (AllowAny, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = [ 'trip_title', 'city', 'state,' ]


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    permission_classes = (TripIsOwnerOrReadOnly, )
    serializer_class = TripDetailSerialzier