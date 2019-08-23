from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class lecture(models.Model):
    grade = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)]) # 학년
    lec_num = models.CharField(max_length = 5) # 강좌번호
    lec_title = models.CharField(max_length = 80) # 교과목명
    lec_num2 = models.CharField(max_length = 20) # 교과목 번호
    lec_value = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)]) # 학점
    lec_time = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)]) # 시간
    lec_prof = models.CharField(max_length = 15) # 담당 교수
    lec_success = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)]) # 신청 인원
    lec_limit = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)]) # 제한 인원
    lec_stair = models.CharField(max_length = 5) # 강의 단계
    lec_time2 = models.CharField(max_length = 150) # 강의 시간
    
    def __str__(self):
        return self.lec_num