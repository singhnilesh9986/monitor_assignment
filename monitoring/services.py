import re
from django.utils.dateparse import parse_datetime
from .models import Keyword, ContentItem, Flag

def calculate_score(keyword_name, title, body):
    """
    Implements the scoring mechanism[cite: 40]:
    - Exact match in title: 100 [cite: 41]
    - Partial match in title: 70 [cite: 42]
    - Match in body: 40 [cite: 43]
    """
    kw = keyword_name.lower()
    t = title.lower()
    b = body.lower()

    if re.search(rf'\b{re.escape(kw)}\b', t):
        return 100
    elif kw in t:
        return 70
    elif kw in b:
        return 40
    return 0

def run_content_scan(content_data):
    """
    Handles the critical Suppression Logic[cite: 50, 51].
    """
    keywords = Keyword.objects.all()
    
    for item in content_data:
        # FIX: Convert the string from mock_data into a real datetime object
        last_updated_dt = parse_datetime(item['last_updated'])

        content_obj, created = ContentItem.objects.update_or_create(
            title=item['title'],
            defaults={
                'body': item['body'],
                'source': item['source'],
                'last_updated': last_updated_dt
            }
        )

        for kw in keywords:
            score = calculate_score(kw.name, content_obj.title, content_obj.body)
            
            if score > 0:
                flag = Flag.objects.filter(keyword=kw, content_item=content_obj).first()
                
                # SUPPRESSION RULE[cite: 52]: 
                # If irrelevant, stay suppressed unless content is newer [cite: 54]
                if flag and flag.status == 'irrelevant':
                    # This comparison now works because both are datetime objects
                    if content_obj.last_updated > flag.created_at:
                        flag.status = 'pending'
                        flag.score = score
                        flag.save()
                elif not flag:
                    Flag.objects.create(keyword=kw, content_item=content_obj, score=score)