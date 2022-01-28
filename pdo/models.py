from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Batch(models.Model):
    barch_id = models.IntegerField(primary_key=True)
    batch_name = models.CharField(max_length=30)
    batch_slug = models.SlugField(unique=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)
    #add_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.batch_slug = slugify(self.batch_name)
        super(Batch, self).save(*args, **kwargs)

    def __str__(self):
        return self.barch_id+self.batch_name+self.is_active

# @receiver(pre_save, sender=Store)
# def batch_pre_save(sender, instance, *args, **kwargs):
#     if not instance.batch_slug:
#         instance.batch_slug = slugify(instance.batch_name)
