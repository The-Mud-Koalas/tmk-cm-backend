from django.db import models
from rest_framework import serializers
from event.models import Event
import uuid


class Forum(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)

    def get_event(self) -> Event:
        return self.event

    def create_post(self, content, author, sentiment_score, is_anonymous=False):
        self.get_event().update_average_forum_post_sentiment_score(sentiment_score)
        return self.forumpost_set.create(
            content=content,
            author=author,
            is_anonymous=is_anonymous,
            sentiment_score=sentiment_score
        )


class ForumPost(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    forum = models.ForeignKey('forums.Forum', on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)
    upvoters = models.ManyToManyField('users.User', related_name="upvoted_posts")
    downvoters = models.ManyToManyField('users.User', related_name="downvoted_posts")
    sentiment_score = models.FloatField(default=0)

    @property
    def author_name(self):
        return "Anonymous User" if self.is_anonymous else self.author.full_name


class ForumSerializer(serializers.ModelSerializer):
    event_name = serializers.ReadOnlyField(source='event.name')
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Forum
        fields = [
            'id',
            'event',
            'event_name',
            'type_display'
        ]


class ForumPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(read_only=True)

    class Meta:
        model = ForumPost
        fields = [
            'id',
            'content',
            'author',
            'author_name',
            'forum',
            'posted_at',
            'is_anonymous',
            'vote_count',
            'upvoters',
            'downvoters'
        ]