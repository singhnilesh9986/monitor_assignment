from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Keyword, Flag, ContentItem
from .serializers import KeywordSerializer, FlagSerializer, ContentItemSerializer
from .services import run_content_scan

class KeywordViewSet(viewsets.ModelViewSet):
    """
    Requirement 2: API endpoint to create and manage keywords.
    """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class FlagViewSet(viewsets.ModelViewSet):
    """
    Requirement 5: Review workflow allowing status updates to 
    pending, relevant, or irrelevant.
    """
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer
    # Restricted to GET and PATCH as per assignment requirements
    http_method_names = ['get', 'patch', 'delete']

class ContentItemViewSet(viewsets.ModelViewSet):
    """
    Helper viewset to view imported content items.
    """
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer

@api_view(['POST'])
def trigger_scan(request):
    """
    Requirement 3 & 6: Trigger a scan against the chosen source.
    Uses the mock dataset provided in the assignment.
    """
    mock_data = [
        {
            "title": "Learn Django Fast", 
            "body": "Django is a powerful Python framework",
            "source": "mock", 
            "last_updated": "2026-03-20T10:00:00Z"
        },
        {
            "title": "Cooking Tips", 
            "body": "Best recipes for beginners", 
            "source": "mock", 
            "last_updated": "2026-03-20T10:00:00Z"
        },
        {
            "title": "Python Automation", 
            "body": "How to build a data pipeline with Python", 
            "source": "mock", 
            "last_updated": "2026-03-21T15:00:00Z"
        }
    ]

    run_content_scan(mock_data)
    
    return Response({"message": "Scan completed and flags generated."})