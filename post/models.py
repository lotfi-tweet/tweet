from django.db import models
from django.contrib.auth.models import User
import random
import os
from django.urls import reverse

class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return  self.cat_name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 354582565415)
    name, ext    = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/{new_filename}/{final_filename}".format(
        new_filename=new_filename, final_filename=final_filename,
    )



class AdsPersonal(models.Model):
    writer = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    ads_p1 = models.TextField(blank=True)
    ads_p2 = models.TextField(blank=True)
    ads_p3 = models.TextField(blank=True)
    imag_p = models.ImageField(upload_to=upload_image_path, blank=True)

    def __str__(self):
        return  self.writer.username


class Post(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title     = models.CharField(max_length=300)
    pup_date  = models.DateTimeField(auto_now_add=True)
    writer    = models.ForeignKey(AdsPersonal, on_delete=models.CASCADE, null=True)
    text_1    = models.TextField(blank=True)
    img_1     = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    visit_num = models.PositiveIntegerField(default=1)
    text_2    = models.TextField(blank=True)
    img_2     = models.ImageField(upload_to=upload_image_path, blank=True)
    img_3     = models.ImageField(upload_to=upload_image_path, blank=True,)
    img_4     = models.ImageField(upload_to=upload_image_path, blank=True,)
    text_3    = models.TextField(blank=True)
    relate1_url = models.URLField(max_length=2000, blank=True)
    title_url1  = models.CharField(max_length=100, blank=True)
    relate2_url = models.URLField(max_length=2000, blank=True)
    title_url2  = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])



class About(models.Model):
    about_as = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

class AdsPublic(models.Model):
    ads_1     = models.TextField(blank=True)
    ads_2     = models.TextField(blank=True)
    ads_3     = models.TextField(blank=True)
    ads_4     = models.TextField(blank=True)
    ads_5     = models.TextField(blank=True)
    ads_6     = models.TextField(blank=True)



class Discount(models.Model):
    mob_name  = models.CharField(max_length=200)
    imag_dics = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    dis_phone = models.TextField()
    date_pup  = models.TimeField(auto_now_add=True)

    def __str__(self):
        return  self.mob_name

    def save(self, *args, **kwargs):
        self.mob_name = self.mob_name.upper()
        return super(Discount, self).save(*args, **kwargs)


