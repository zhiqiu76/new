from django.db import models

# Create your models here.


"""部门"""
class Dept(models.Model):
    deptNo = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50, null=True, db_index=True, unique=True)
    loc = models.CharField(max_length=100)
    class Meta:
        db_table = 'dept'


"""员工信息"""
class Emp(models.Model):


    empNo = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=20, null=False, db_index=True)
    job = models.CharField(max_length=20, null=True, db_index=False)
    # 上一级领导,db_constraint=False就不在数据库层面设置约束
    mgr = models.ForeignKey('self', on_delete=models.DO_NOTHING, db_constraint=False, db_column="mgr", null=True)
    hireDate = models.DateField(null=True)
    sal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    comm = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    # 部门编号
    dept = models.ForeignKey(Dept, on_delete=models.DO_NOTHING, db_column="deptno", db_constraint=False, null=True)

    gender_choices = [
        (0, '女'),
        (1, '男')
    ]
    gender = models.IntegerField(choices=gender_choices, null=True)
    is_valid_choices = [
        (0, '无效'),
        (1, '有效')
    ]
    isValid = models.IntegerField(default=1, choices=is_valid_choices, db_column="is_valid")

    class Meta:
        db_table = 'emp'
        # ordering = ['empNo']


class SalGrade(models.Model):
    grade = models.AutoField(primary_key=True)
    lowsal = models.IntegerField()
    higsal = models.IntegerField()
    class Meta:
            db_table = 'salegrade'


