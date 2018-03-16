# !/usr/bin/python
# -*-coding:utf-8-*-
# class People(object):
     
#     def __init__(self, name, age, weight):
#          self.name = name
#          self.age = age
#          self.__weight = weight

#     def info(self):
#         print "我叫 %s 今年 %d 岁了! " % (self.name, self.age)


# class Student(People):
#     classroomid = 324
#     address = "西安市雁塔区高新一中"
     
#     def __init__(self, name, age, weight, grade):
#          People.__init__(self, name, age, weight)
#          self.grade = grade

#     def info(self):
#         print "大家好！ 我叫 %s 今年 %d 岁了，%s年级了, \
#         以后就是一个班的同学请大家多多关照！ " % (self.name, self.age, self.grade)


# student = Student("Lisa", 15, 60, "初二")
# student.info()

class A(object):
    def __init__(self, name):
        self.name = name
        print "进入了父类初始化方法"

    def show(self):
        print "进入了父类show() 名称为: %s" % self.name

class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name)
        self.age = age

    def show(self):
        super(B, self).show()
        

b = B("Masa", 25)
b.show()



    server {
        listen       80 default_server;
        # listen       [::]:80 default_server;
        server_name  api.hixinma.top;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        #include /etc/nginx/default.d/*.conf;

        location / {
            root /var/www/project/www.wangda/wangda;       # 项目根目录
            proxy_ignore_client_abort on;
            include  uwsgi_params;
            uwsgi_pass  127.0.0.1:9090;             # 必须和uwsgi中的设置一致
            uwsgi_param UWSGI_SCRIPT /var/www/project/www.wangda.wsgi;  # 入口文件，即wsgi.py相对于项目根目录的位置，“.”相当于一层目录
            index  index.html index.htm;
            client_max_body_size 35m;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
