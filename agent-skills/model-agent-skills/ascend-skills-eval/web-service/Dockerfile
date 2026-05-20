# 本地：在仓库根执行 docker build -f web-service/Dockerfile .
# Zeabur 使用仓库根目录的 Dockerfile（平台自动检测根路径）。
FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

WORKDIR /app

COPY web-service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY web-service/app /app/app
COPY skills/skills-eval /app/skills/skills-eval

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

EXPOSE 8080

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
