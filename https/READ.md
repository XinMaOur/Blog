## 编译时指定 –with-http_ssl_module(如果已经编译过了,可以再次编译)

### 不然会报以下错：
> nginx: [emerg] unknown directive "ssl" in /usr/local/nginx/conf/conf.d/ssl.conf:8
     
默认情况下ssl模块并未被安装，如果要使用该模块则需要在编译时指定–with-http_ssl_module参数，安装模块依赖于OpenSSL库和一些引用文件，通常这些文件并不在同一个软件包中。通常这个文件名类似libssl-dev。

## 生成证书
可以通过以下步骤生成一个简单的证书：
首先，进入你想创建证书和私钥的目录，例如：
> $ cd /usr/local/nginx/conf
## 1.创建服务器私钥,命令会让你输入一个口令：
> $ openssl genrsa -des3 -out server.key 1024

## 2.创建签名请求的证书（CSR）：
> $ openssl req -new -key server.key -out server.csr

## 3.在加载SSL支持的Nginx并使用上述私钥时除去必须的口令：

> $ cp server.key server.key.org
> $ openssl rsa -in server.key.org -out server.key

## 4.配置nginx
最后标记证书使用上述私钥和CSR：

> $ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
