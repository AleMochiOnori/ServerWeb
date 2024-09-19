FROM python:3.10-alpine
ADD server.py .
ADD requirements.txt .
RUN pip install flask
ADD ./templates/index.html ./templates
ADD ./templates/index2.html ./templates

CMD ["python", "server.py"]
