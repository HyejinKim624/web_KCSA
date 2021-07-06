from django.db import models

# Create your models here.
class VoiceFile(models.Model):
    fname = models.CharField(max_length=50)         # 파일 이름
    fnExtension = models.CharField(max_length=10)   # 파일 확장자