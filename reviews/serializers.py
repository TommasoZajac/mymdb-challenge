from rest_framework import serializers
from reviews.models import Review
from movies.models import Movie,Character
from cast.models import Person


class ReviewRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        #print(value.__str__(), " ", isinstance(value, Movie), " ", type(value))

        if isinstance(value, (Movie, Character, Person)):
            return value.__str__()
        raise Exception('Unexpected type of tagged object')

class ReviewSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    content_object = ReviewRelatedField(many=False, read_only=True)
    class Meta:
        model = Review
        fields = ('id','text','content_object','created_at','updated_at')

class ReviewCreateSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Review
        fields = ('id','text','content_type','object_id')