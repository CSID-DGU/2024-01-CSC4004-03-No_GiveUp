from django.db import models
from signup.models import User

#사용자 음역대 파일 이름 저장하는 모델
class UserMaxMinFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    min_file = models.FileField(upload_to='userVoice/')
    max_file = models.FileField(upload_to='userVoice/')

class UserMaxMinNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #signup으로 로그인한 유저의 보컬분석후 음역대 정보 저장하기
    max_note = models.CharField(max_length=50, default = "none")
    min_note = models.CharField(max_length=50, default = "none")