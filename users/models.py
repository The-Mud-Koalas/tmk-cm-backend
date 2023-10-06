from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from .managers import UserManager


class User(AbstractUser):
    username = None
    password = None
    email = None

    last_login = None
    first_name = None
    last_name = None

    user_id = models.CharField(max_length=30, unique=True, primary_key=True)
    full_name = models.CharField(max_length=50, null=True)
    reward_points = models.IntegerField(default=0)
    preferred_radius = models.FloatField(default=2000)
    location_track = models.BooleanField(default=True)

    notified_locations = models.ManyToManyField('space.Location', through='users.NotifiedLocation')
    interests = models.ManyToManyField('event.Tags')

    USERNAME_FIELD = 'user_id'

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.user_id

    def set_full_name(self, full_name):
        self.full_name = full_name
        self.save()

    def set_preferred_radius(self, preferred_radius):
        self.preferred_radius = preferred_radius
        self.save()

    def set_location_track(self, location_track):
        self.location_track = location_track
        self.save()

    def add_to_notified_locations(self, location, is_subscribe):
        existing_notified_location = self._get_notified_location_objects().filter(location=location)
        if not existing_notified_location.exists():
            NotifiedLocation.objects.create(
                user=self,
                location=location,
                subscribed=is_subscribe
            )

        else:
            existing_notified_location = existing_notified_location[0]
            existing_notified_location.update_subscription(is_subscribe)

    def _get_notified_location_objects(self):
        return NotifiedLocation.objects.filter(user=self)

    def get_notified_locations(self):
        return list(map(lambda x: x.location, self._get_notified_location_objects()))

    def get_subscribed_locations(self):
        return list(map(lambda n: n.location, self._get_notified_location_objects().filter(subscribed=True)))

    def get_user_id(self):
        return str(self.user_id)

    def get_interests(self):
        return self.interests.all()

    def get_preferred_radius(self):
        return self.preferred_radius

    def set_interests(self, interests):
        self.interests.clear()
        for interest in interests:
            self.interests.add(interest)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'full_name',
            'reward_points',
            'preferred_radius',
            'location_track'
        ]


class NotifiedLocation(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    location = models.ForeignKey('space.Location', on_delete=models.RESTRICT)
    subscribed = models.BooleanField(default=False)

    def update_subscription(self, subscribed):
        self.subscribed = subscribed
        self.save()

