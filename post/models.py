from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别名称')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = '类别'

    def __str__(self):
        return 'Category:%s' % self.cname


class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name='标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = '标签'

    def __str__(self):
        return 'Tag:%s' % self.tname


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = '帖子'

    def __str__(self):
        return 'Post:%s' % self.title
