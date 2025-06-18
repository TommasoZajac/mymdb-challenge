from rest_framework import serializers
from reviews.models import Review
from movies.serializers import MovieSerializer
"""
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'owner', 'title', 'code', 'linenos', 'language', 'style']

"""
class ReviewSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    movie = MovieSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        fields = ['id','text','content_type','created_at','updated_at']