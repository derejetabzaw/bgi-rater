from karaoke import models, serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rater import audio_rater

class Record_Audio(generics.ListCreateAPIView):
    """
    view which handle incoming request with audio file
    """
    queryset = models.RecordedAudio.objects.all()
    serializer_class = serializers.RecordedAudioSerializer

    def post(self, request):
        serializer = serializers.RecordedAudioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # call the rater function and return the song and confidence level as a response
        # recorded_audio = serializer.data["audio"]
        # song_name, confidence = audio_rater.song_rator(recorded_audio)
        # return Response({
        #     "song_name": song_name,
        #     "confidence": confidence
        #     })
        return Response ({"data": serializer.data})


