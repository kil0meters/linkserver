FROM python:3.12-rc-alpine
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "server.py"]
