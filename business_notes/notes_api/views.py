from django.shortcuts import render
from rest_framework.views import APIView, Response

from notes_app.models import Note
from .serializers import NoteListSerializer


class NotesListAPIView(APIView):
    def get(self, request):
        resp = Note.objects.all()
        return Response(NoteListSerializer(
            instance=resp,
            many=True).data
        )

