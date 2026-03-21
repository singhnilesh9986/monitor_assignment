from rest_framework import serializers
from .models import Keyword, ContentItem, Flag

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']

class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = ['id', 'title', 'source', 'body', 'last_updated']

class FlagSerializer(serializers.ModelSerializer):
    # These 'ReadOnlyFields' allow us to see names instead of just ID numbers
    keyword_name = serializers.ReadOnlyField(source='keyword.name')
    content_title = serializers.ReadOnlyField(source='content_item.title')

    class Meta:
        model = Flag
        fields = ['id', 'keyword', 'keyword_name', 'content_item', 'content_title', 'score', 'status']
        # The user shouldn't manually set the score; the system calculates it
        read_only_fields = ['score']