from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post, PostComment


@receiver(m2m_changed, sender=Post.likes.through)
def update_post_like_count(sender, instance, **kwargs):
    instance.like_count = instance.likes.count()
    instance.save()


@receiver(m2m_changed, sender=PostComment.likes.through)
def update_post_comment_like_count(sender, instance, **kwargs):
    instance.likes_count = instance.likes.count()
    instance.save()