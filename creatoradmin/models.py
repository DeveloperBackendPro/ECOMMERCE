from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.core.validators import FileExtensionValidator

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(upload_to='images/Admin',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Creator)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Creator.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)

    def user_name(self):
        return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'





class Client(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True,null=True)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/Clients',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')

    def __str__(self):
        return self.user.username

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Client)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Client.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


    def user_name(self):
        return self.user.first_name + '' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


