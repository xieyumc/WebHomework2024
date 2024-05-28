# 使用Python官方镜像
FROM python:3.11.9-slim-bullseye

# 设置工作目录
WORKDIR /app

# 安装系统依赖
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends gcc \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# 复制requirements.txt并安装依赖
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt


# 复制项目文件
COPY . .
COPY ../.env /usr/src/app/.env

# 暴露端口
EXPOSE 8000

# 启动Django应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]