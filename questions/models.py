from django.db import models

# Create your models here.


# 创建一个Question类- 对应的是数据库的表名
class Question(models.Model):
    # 创建一个question_text字段，是varchar(200)
    question_text = models.CharField(max_length=200)
    # 创建一个pub_date字段，是datetime类型
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def show(self):
        return "这是个问题【%s】?" % self.question_text
