from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


# 创建一个Question类- 对应的是数据库的表名
class Question(models.Model):
    # 创建一个question_text字段，是varchar(200)
    question_text = models.CharField(max_length=200)
    # 创建一个pub_date字段，是datetime类型
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


     # 是否是近一天发布的
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 创建一个Choice类- 对应的是数据库的表名，Question和Choice是一对多的关系
class Choice(models.Model):
    # 创建一个外键关联Question表
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="choice", related_query_name="choices")
    # 创建选项内容，是varchar类型长度是200
    choice_text = models.CharField(max_length=200)
    # 创建投票数量字段，是int类型，默认是0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

