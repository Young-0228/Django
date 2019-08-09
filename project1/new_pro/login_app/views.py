import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here
# 全部导进来
from .models import *
# 登录视图

# 登陆渲染——》路径
def show_login(request):

    return render(request,"login/login.html")

#注册渲染———》路径
def show_register(request):

    return render(request,"login/register.html")

# 添加数据
# 获取数据用户名和密码--》判断用户名和密码是否为空--》1.如果用户名和密码为空，返回错误
# 获取数据用户名和密码--》判断用户名和密码是否为空--》2.用户名密码不为空--》判断用户名是否已存在--》1不存在--》向数据库添加信息
# 获取数据用户名和密码--》判断用户名和密码是否为空--》2.用户名密码不为空--》判断用户名是否已存在--》2存在--》返回错误
@csrf_exempt
def add_data(request):
    name = request.POST.get("username")
    password = request.POST.get("password")
    print(len(name))
    print(len(password))
    if name == "" or password == "":
        # 不能添加数据
        return HttpResponse(json.dumps({"code":400,"msg":"用户名或密码不能为空"}))
    else:
        #  用户名不为空
        num = SuperSchool.objects.filter(account=name).count()
        if num <=0:
            # 数据库用户名不存在，添加数据
            SuperSchool.objects.create(account=name,secret=password)
            return HttpResponse(json.dumps({"code":200,"msg":"添加数据成功"}))
        else:
            return HttpResponse(json.dumps({"code":500,"msg":"用户名已存在，请直接登陆"}))

def check_data(request):
    # 获取login网页中的应户名和密码
    name = request.GET.get("username")
    password = request.GET.get("password")
    # 根据login中获取的用户名和密码，提起数据库存在相对应的用户名和密码
    # 获取数据库中所有信息 list
    # list1 = SuperSchool.objects.all()
    # list2 = []
    # # 遍历列表list1
    # for i in list1:
    #     # 讲每个列表中的名字加入一个新的列表中
    #     list2.append(i.account)
    # if name in list2:
    #     new_name = SuperSchool.objects.get(account=name)
    # 异常处理
    # try--except--else--finally
    # try: 检查是否有报错信息，讲检查代码放到try下
    # except :如果有报错，执行except下的代码  同if else,很像
    #else；try中代码，正常执行，会走else下的代码
    #finally: 最后的，在try异常处理中，不管会不会有报错信息，都会走finally下的代码
    try:
        new_name = SuperSchool.objects.get(account=name)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"code": 400, "msg": "用户名或密码不存在"}))
    # 在try正长执行，才会执行else
    else:
        # 判断login中，用户名是否存在
        if new_name == "":
            return HttpResponse(json.dumps({"code":500,"msg":"用户名或密码错误"}))
        else:
            # 以用户名为搜索条件，获得其中用户名所在的一条数据，即对象
            # obj = SuperSchool.objects.filter(account=new_name)
            # 对象中获取密码，判断是否是login中输入的密码
            # b = new_name.secret
            # # a = obj.secret
            # print(obj)
            # print(type(obj))
            # print(obj.secret)
            if new_name.secret == password:
                return HttpResponse(json.dumps({"code":200,"msg":"用户名和密码正确，登录首页"}))
    # else:
    #     return HttpResponse(json.dumps({"code":400,"msg":"用户名或密码不存在"}))

# 渲染首页
def show_home(request):
    return render(request,"detail/home_page.html")

# 获取战斗学宫的全部名字
@csrf_exempt
def get_room_name(request):
    # 获取战斗学宫全部数据
    try:
        c_names = Clossroom.objects.all()
    except Exception as e:
        print(e)
    # 推导式：快速建立数组
    # for item in c_names:
    #     list.append(item.c_name)
    c_name = [item.c_name for item in c_names]
    return HttpResponse(json.dumps(c_name))

# 添加召唤师
@csrf_exempt
def add_student(request):
    print(request.method)
    if request.method == "POST":
        id = request.POST.get("s_id")
        name = request.POST.get("s_name")
        tel = request.POST.get("s_tel")
        gender = request.POST.get("gender")
        # classroom是一对多中的外键
        classroom = request.POST.get("study")
        # 以外键为标准获取classroom里的对象
        classobj = Clossroom.objects.filter(c_name=classroom).first()
        try:
            Student.objects.create(s_id=id,s_name=name,s_tel=tel,s_gender=gender,s_classroom=classobj)
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"code": 500, "msg": "召唤师添加时，服务器错误"}))
        return  HttpResponse(json.dumps({"code":200,"msg":"召唤师添加成功"}))
    else:
        return HttpResponse(json.dumps({"code": 400, "msg": "召唤师添加时，内部服务器报错"}))

# 获取最强王者
def get_hero(request):
    try:
        heros = Teacher.objects.all()
    except Exception as e:
        print(e)
#     用推导式获取列表
    t_name = [item.t_name for item in heros]
    print(t_name)
    return HttpResponse(json.dumps(t_name))

# 添加王者老师和课程
@csrf_exempt
def add_course(request):
    if request.method == "POST":
        id = request.POST.get("c_id")
        name = request.POST.get("c_name")
        tea_name = request.POST.get("gender")
        score = request.POST.get("study")
        tea_obj = Teacher.objects.filter(t_name=tea_name).first()
        try:
            obj = Course.objects.create(co_id=id,co_name=name,co_score=score)
            obj.co_teacher.set([tea_obj])
            obj.save()
            return HttpResponse(json.dumps({"code": 200, "msg": "添加王者成功"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"code":500,"msg":"添加王者，数据内部错误"}))
    else:
        return HttpResponse(json.dumps({"code":400,"msg":"添加王者，服务器内部错误"}))


# 获取战斗学宫班级名
def get_name_class(request):
    try:
        obj_list = Clossroom.objects.all()
    except Exception as e:
        print(e)
#    推导式
    c_names = [item.c_name for item in obj_list]
    return HttpResponse(json.dumps(c_names))

#获取每个战斗学宫班对应的老师
def get_tea_name(request):
    try:
        name = request.GET.get("study")
        print("c_name:{0}".format(name))
        c_closs_tea = Clossroom.objects.filter(c_name=name).first()
        print("c_tea:{0}".format(c_closs_tea))
        tea_list = [{"id":item.t_id,"name":item.t_name} for item in c_closs_tea.c_teacher.all()]
    except Exception as e:
        print(e)
    return HttpResponse(json.dumps(tea_list))

# 王者峡谷数据添加
# 班级添加
@csrf_exempt
def add_classroom(request):
    if request.method=="POST":
        id = request.POST.get("c_id")
        class_name = request.POST.get("study")
        teacher_name = request.POST.get("study1")
        # 寒冰女王艾希(h1002)
        print(teacher_name)
        name1 = "寒冰女王艾希(h1002)"
        # replace js字符串操作 三个参数，1正则，2删掉内容，3替换内容
        # replace( / name1 / g, "寒冰女王艾希")
        name1 = teacher_name[0:6:1]
        print(name1)
        try:
            # 老师类列表
            teacher_obj = Teacher.objects.filter(t_name=name1).first()
            print(teacher_obj)
            # 班级类列表
            class_obj = Clossroom.objects.create(c_id=id)
            # 班级类列表中添加老师类列表
            class_obj.c_teacher.set([teacher_obj])
            class_obj.save()
            return HttpResponse(json.dumps({"code": 200, "msg": "班级添加成功"}))
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"code":500,"msg":"班级添加，数据库错误"}))
    else:
        return HttpResponse(json.dumps({"code": 400, "msg": "班级添加，服务器内部错误"}))