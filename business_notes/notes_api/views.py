from django.shortcuts import render
from rest_framework.views import APIView, Response

class NotesListAPIView(APIView):
    def get(self, request):
        return Response({})

