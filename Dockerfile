FROM python:3.7

RUN mkdir /app
RUN mkdir /run/conjur
WORKDIR /app
ADD . /app/
CMD ["python3", "/app/main.py"]
