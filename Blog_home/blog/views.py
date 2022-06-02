from django.shortcuts import render
from rest_framework.views import Response, APIView

from .models import BLOGS


class BlogAPIView(APIView):
    def get(self, request):
        return Response(data=BLOGS)

    def post(selfself, request):
        new_blog = request.data
        BLOGS.append(new_blog)
        return Response(data=new_blog)

    def put(selfself, request):
        ...
