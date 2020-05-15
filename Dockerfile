FROM python:3.6-alpine

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
