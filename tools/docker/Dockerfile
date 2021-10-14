FROM python:3.9

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/* /app/requirements/
RUN pip install -r requirements/base.txt
RUN pip install -r requirements/development.txt
RUN pip install -r requirements/production.txt

ADD . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
