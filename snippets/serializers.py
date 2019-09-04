from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet,LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.username')
   url = serializers.CharField(source='get_absolute_url', read_only=True)
   class Meta:
       model = Snippet
       fields = ['id','url', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']