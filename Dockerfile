FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV ENV 'LOCAL'
ENV DB_HOST '172.17.0.1'

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000
EXPOSE 5432

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]