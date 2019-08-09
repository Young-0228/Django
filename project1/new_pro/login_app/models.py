from django.db import models

# Create your models here.

# 定义数据库 登陆注册用户名
class SuperSchool(models.Model):
    account = models.CharField(max_length=100,null=False,blank=False,verbose_name="用户名")
    secret = models.CharField(max_length=100,null=False,blank=False,verbose_name="密码")

    class Meta:
        db_table = "SuperSchool"
        verbose_name = "超神学院"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.account

# 在数据库迁移时，会后跟上app应用名，表示只能迁移本应用app数据库
# 但，第一数据库迁移，需要django文件，不能加app应用名
# 老师，最强王者
class Teacher(models.Model):
    t_id = models.CharField(max_length=32,null=False,blank=False,verbose_name="最强王者编号")
    t_name = models.CharField(max_length=32,null=False,blank=False,verbose_name="最强王者称号")
    t_num = models.IntegerField(default=0,verbose_name="最强王者收徒数")

    class Meta:
        db_table = "Teacher"
        verbose_name = "最强王者表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.t_name
# 定义战斗学宫 班级 五个办，上中，下野，辅助
class Clossroom(models.Model):
    c_id = models.CharField(max_length=32,null=False,blank=False,verbose_name="战斗学宫编号")
    c_name = models.CharField(max_length=32,null=False,blank=False,verbose_name="战斗学宫名")
    c_teacher = models.ManyToManyField(Teacher,verbose_name="多对多关联老师")
    class Meta:
        db_table = "Clossroom"
        verbose_name = "战斗学宫"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name

# 定义召唤师数据库模型 学生，添加召唤师
class Student(models.Model):
    s_id = models.CharField(max_length=32,null=False,blank=False,verbose_name="召唤师学号")
    s_name = models.CharField(max_length=32,null=False,blank=False,verbose_name="召唤师名称")
    s_tel = models.IntegerField(default=0,verbose_name="召唤师麦段")
    s_gender = models.CharField(max_length=10,verbose_name="召唤师性别")
    s_classroom = models.ForeignKey(Clossroom,on_delete=models.SET_NULL,null=True,verbose_name="关联战斗学宫")

    class Meta:
        db_table = "Student"
        verbose_name = "召唤师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_name

# 定义学习战场定位  课程教学，打那一路 战场名，学习课程名字 ，学习上，中下野辅助
# 班级里有学生，班级里有老师，班级有名字，班级有课程
# python班，Python老师，教python，学生学python
class Course(models.Model):
    co_id = models.CharField(max_length=32,null=False,blank=False,verbose_name="战场辨明")
    co_name = models.CharField(max_length=32,null=False,blank=False,verbose_name="战场名")
    co_teacher = models.ManyToManyField(Teacher,verbose_name="关联最强王者")
    co_score = models.CharField(max_length=10,verbose_name="几杀")

    class Meta:
        db_table = "Course"
        verbose_name = "战场定位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.co_name


















