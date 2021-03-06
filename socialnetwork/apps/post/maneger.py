from math import floor

from django.db import models
from django.utils.timezone import now


class PostManege(models.Manager):
    def life_time(self, time):
        lifetime = (now() - time).total_seconds()

        hour = lifetime / 3600
        if hour < 1:
            return 'A little while ago'
        if hour < 24:
            return str(floor(lifetime / 3600)) + " hour"
        month = lifetime / 2628000
        if month < 1:
            return str(floor(lifetime / 86400)) + " days"
        year = lifetime / 31536000
        if year < 1:
            return str(floor(lifetime / 2628000)) + ' month'
        if year > 1:
            return str(floor(lifetime / 31536000)) + " year"


class CommentManager(models.Manager):
    """
    delete comment
    input : comment id, The user ID entered
    """

    def delete_comment(self, comment_pk, login_user_pk):
        author = self.filter(pk=comment_pk).values("user")
        if author[0]['user'] == login_user_pk:
            self.filter(pk=comment_pk).delete()
            return True
        else:
            return False
