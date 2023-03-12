from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#用户学习的主题
class Topic(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    #返回模型的字符串表示
    def __str__(self):
        return self.text

#学到的有关某个主题具体知识
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    #返回模型的字符串表示
    def __str__(self):
        return self.text[:50] + "..."
