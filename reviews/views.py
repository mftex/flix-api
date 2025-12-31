from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewRetriveUpdateDestroySerializer
from rest_framework import generics


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewRetriveUpdateDestroySerializer
    
