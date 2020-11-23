from karaoke import models, serializers
from rest_framework import generics, status
from rest_framework.response import Response

class Record_Audio(generics.ListCreateAPIView):
    """
    view which handle incoming request with audio file
    """
    queryset = models.RecordedAudio.objects.all()
    serializer_class = serializers.RecordedAudioSerializer

    def post(self, request):
        return self.create(request)


