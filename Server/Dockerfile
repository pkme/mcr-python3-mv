# 基础镜像：python3.8镜像
FROM python:3.8

# 镜像维护者的姓名和邮箱地址
MAINTAINER swd  <736202234@qq.com>

#添加本地文件到镜像中
ADD . /Server

# 工作目录
WORKDIR /Server

# 默认显示help帮助信息
CMD ["-python Server.py"]