from rest_framework import serializers
from movies.models import Character,Movie

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
class MovieSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = ['id','title','description','created_at','updated_at']

class CharacterSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    movie = serializers.SlugRelatedField(slug_field='title', many=False, read_only=True)
    person = serializers.CharField(source = "person_name", read_only=True)

    class Meta:
        model = Character
        fields = ['id','name','movie','person','created_at','updated_at']

