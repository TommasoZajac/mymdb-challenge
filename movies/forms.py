from django.forms import ModelForm
from movies.models import Character

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name","person"]


    