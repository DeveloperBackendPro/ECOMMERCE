from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from colorfield.fields import ColorField
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.core.validators import FileExtensionValidator
from django.db.models import Avg, Count
########################################################################################################################
########################################################################################################################
########################################################################################################################
class Category(MPTTModel):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    parent = TreeForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/Category',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Category)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Category.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)

class MPTTMeta:
    order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])
########################################################################################################################
########################################################################################################################
########################################################################################################################
class Product(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Product',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    old_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Product)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Product.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)



    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})





class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/Pro-details',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    collor = ColorField()
    size = models.CharField(max_length=200)
    def __str__(self):
        return self.size

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Images)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Images.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)



class Comment(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=True)
    subject = models.CharField(max_length=55, blank=True)
    email = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=255,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name