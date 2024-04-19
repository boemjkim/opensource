from django.db import models

# Create your models here.

class Todo(models.Model):		#model명은 자유이나, 괄호 안 내용은 필수
    content = models.CharField(max_length=255) 	#테이블생성과 유사, 여기에 입력된 데이터를 쌓음