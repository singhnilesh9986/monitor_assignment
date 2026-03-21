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
    keyword_name = serializers.ReadOnlyField(source='keyword.name')
    content_title = serializers.ReadOnlyField(source='content_item.title')

    class Meta:
        model = Flag
        fields = ['id', 'keyword', 'keyword_name', 'content_item', 'content_title', 'score', 'status']
        read_only_fields = ['score']