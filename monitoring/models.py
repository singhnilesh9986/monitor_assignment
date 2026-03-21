from django.db import models

class Keyword(models.Model):
    """
    Stores the specific words or phrases the user wants to monitor.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ContentItem(models.Model):
    """
    Stores articles or posts fetched from external sources.
    """
    title = models.CharField(max_length=500)
    body = models.TextField()
    source = models.CharField(max_length=100)
    # This timestamp is critical for the 'Suppression' rule logic later
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.title

class Flag(models.Model):
    """
    The link between a Keyword and a ContentItem with a calculated score.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('relevant', 'Relevant'),
        ('irrelevant', 'Irrelevant'),
    ]

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    score = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevents creating multiple flags for the same keyword on the same article
        unique_together = ('keyword', 'content_item')

    def __str__(self):
        return f"{self.keyword.name} match in {self.content_item.title}"