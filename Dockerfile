FROM python:latest
COPY . /app
CMD ["python", "main.py"]