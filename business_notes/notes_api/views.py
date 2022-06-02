from django.shortcuts import render
from rest_framework.views import APIView, Response

from notes_app.models import Note
from .serializers import NoteListSerializer


class NotesListAPIView(APIView):
    def get(self, request):
        resp = Note.objects.all().order_by("date_and_time", "importance")
        return Response(NoteListSerializer(
            instance=resp,
            many=True).data
        )

