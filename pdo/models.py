from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Batch(models.Model):
    barch_id = models.IntegerField(primary_key=True)
    ttc_name = models.CharField(max_length=200)
    batch_name = models.CharField(max_length=30)
    batch_start_date = models.DateTimeField(blank=True, null=True)
    class_time = models.TimeField(blank=True, null=True)
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

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=60)
    student_fathers_name = models.CharField(max_length=50)
    student_mothers_name = models.CharField(max_length=50)
    student_date_of_birth = models.DateField(default=None)
    student_email = models.EmailField(blank=True, null=True)
    student_passport_number = models.CharField(max_length=10)
    student_mobile_no = models.CharField(max_length=15, blank=True, null=True)
    student_image=models.FileField(upload_to='documents/student_image', blank=True, null=True)
    student_slug = models.SlugField(unique=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.student_slug = slugify(self.student_name)
        super(Student, self).save(*args, **kwargs)


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=30)
    country_flag =models.FileField(upload_to='documents/country_image', blank=True, null=True)
    country_slug = models.SlugField(unique=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.country_slug = slugify(self.country_name)
        super(Country, self).save(*args, **kwargs)


class PDO(models.Model):
    STATUS_LIST = (
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('selected', 'Selected'),
            ('po_approved', 'Principal Approved'),
            ('dg_approved', 'DG Approved'),
            ('completed', 'Completed')
        )
    pdo_id = models.IntegerField(primary_key=True)
    pdo_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    pdo_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    pdo_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    pdo_status = models.CharField(max_length=30, default="Pending", choices=STATUS_LIST)
    created = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    modified = models.DateTimeField(auto_now_add=True, null=True)
    payment_status = models.BooleanField(default=False)


class Payment(models.Model):
    payment_id =models.IntegerField(primary_key=True)
    payment_pdo = models.ForeignKey(PDO, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200)
    payment_amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, null=True)
