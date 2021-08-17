import trip
from django.contrib.auth.models import User
from trip.permissions import TripIsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from trip.models import Trip
from trip.serializers import TripCreateSerializer, TripListSerializer, TripDetailSerialzier, TripUpdateSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView 
from rest_framework.parsers import FormParser, MultiPartParser



class TripCreate(generics.CreateAPIView):
    queryset = Trip.objects.all()
    permission_classes = ( TripIsOwnerOrReadOnly, )
    serializer_class = TripCreateSerializer
    parser_classes = [ MultiPartParser, FormParser ]


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
