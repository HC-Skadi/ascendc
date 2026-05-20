# Zeabur 仅在仓库根目录存在名为 Dockerfile/dockerfile 时才会按 Docker 构建。
# 若只有 web-service/Dockerfile，平台会回退为默认 Caddy(:8080)，运行时日志里只有 Caddy、公网访问易 404。
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
