from .models import Musician
from rest_framework import serializers

class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = "name", "debut_album"

