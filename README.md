# Blog
喜欢git，希望通过github的单个仓库作为Blog来记录新路历程。世上并没有路，走的人多了罢了。

## 1. Env

    OS: Centos7
    Python: 2.7.5(Centos7预装)

### 1.1安装nginx 之前需要安装的库
    yum -y install gcc gcc-c++ ncurses-devel zlib zlib-devel openssl openssl--devel pcre pcre-devel
    
### 1.2 安装uwsgi之前需要安装python-devel
    yum install python-devel  ==>  uwsgi
    
### 1.3 关键包版本
    django=1.11.1
    nginx=1.12.2
    uWSGI=2.0.17
 
## 2.uWSGI
### desc: uWSGI是实现了uwsgi(线路协议)和WSGI(通信协议)两种协议的Web服务器.
    官方文档： https://uwsgi-docs.readthedocs.io/en/latest/Management.html
### 2.1 我采用的ini文件作为启动项(还可以用xml,yaml,环境变量等)
    [uwsgi]
        chdir=/var/www/project/www.wangda/wangda/
        # uid=www-data
        # gid=www-data
        pythonpath=/usr/bin/python2.7
        wsgi-file = wangda/wangda/wsgi.py
        socket = 127.0.0.1:9090
        protocol=http
        master=true
        workers=5
        pidfile=/var/www/project/www.wangda/wangda/uwsgi.pid
        vacuum=true
        thunder-lock=true
        enable-threads=true
        harakiri=30
        post-buffering=4096
        daemonize=/var/www/project/www.wangda/wangda/uwsgi.log
        env = LANG=en_US.UTF-8 
 ### 2.2 所踩的坑
 
 #### 2.2.1 Q：
      如果uwsgi错误中提示:
      *** Operational MODE: preforking ***
      ImportError: No module named {{wangda}}.wsgi
      unable to load app 0 (mountpoint='') (callable not found or import error)
      *** no app loaded. going in full dynamic mode ***
      
 #### 2.2.1 A：  
      chdir 为project目录    
      --wsgi-file 对应project下的同名目录，再下面是wsgi.py,否则系统无法import
      
## 3. nginx
### nginx 性能、性能、性能,apache 稳定、稳定、稳定
### 3.1 配置文件
    server {
          listen       80;
          server_name  api.hixinma.top;

          #charset koi8-r;

          #access_log  logs/host.access.log  main;

          location / {
              root   /var/www/project/www.wangda/wangda;      # 项目根目录
              include  uwsgi_params;
              proxy_pass  http://127.0.0.1:9090/;             # 同uwsgi中配置开启的端口
              index  index.html index.htm;
              client_max_body_size 35m;
          }
          error_log /usr/local/nginx/logs/error.log  error;

          error_page  404              /404.html;

          # redirect server error pages to the static page /50x.html

          error_page 404 /404.html;
              location = /40x.html {
          }

          error_page   500 502 503 504  /50x.html;
              location = /50x.html {
                  root   html;
          }
      }

### 3.2 一个显而易见的坑
  我在调试nginx error.log 之初看不到详细的调试错误信息.
  这需要使用源码包安装nginx,要激活 debug 日志，Nginx 在构建时需要配置为支持 debug：
  
    ./configure --with-debug ...
  然后在 server 层面上重新指定的日志将会禁用这台服务器的 debug 日志：
  
    http {
        server {
            error_log /path/to/log;
            ...
            为了避免这种现象的发生，要么你就注释掉重新定义的那行日志，要么你就在那行也加上 debug 级别：
    error_log /path/to/log debug;

## 4.Django

### 4.1 坑点
    django 直接返回序列化json列表数据,需要借助于第三方插件。   
     
    url：https://github.com/bluedazzle/django-simple-serializer
    
   运行需求
   
     Python 2:
        Django >= 1.5
        Python >= 2.6

     Python 3:
        Django >= 1.8
        Python >= 3
   安装：
    
      pip install django-simple-serializer
