import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Prompt(models.Model):
    # using uuid so ids are not guessable from the frontend
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    content = models.TextField()

    # complexity goes from 1 to 10
    complexity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    # ✅ NEW FIELD (TAGGING SYSTEM)
    tags = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'prompts'
        ordering = ['-created_at']   # latest prompts show first

    def __str__(self):
        return self.title

    def to_dict(self, view_count=None):
        # converting to plain dict so i can return it as json easily
        data = {
            'id':         str(self.id),
            'title':      self.title,
            'content':    self.content,
            'complexity': self.complexity,
            'tags':       self.tags,   # ✅ include tags
            'created_at': self.created_at.isoformat(),
        }

        # view_count only comes in when fetching a single prompt
        if view_count is not None:
            data['view_count'] = view_count

        return data
