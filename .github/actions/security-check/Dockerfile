FROM python:3.10-slim

COPY entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py

ENTRYPOINT [ "python", "/entrypoint.py" ]
