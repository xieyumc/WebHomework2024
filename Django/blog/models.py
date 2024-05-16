from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # 存储Markdown内容
    pub_date = models.DateTimeField('date published')
    cover_url = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title