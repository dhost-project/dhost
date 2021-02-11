FROM python:3.9

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
COPY requirements_dev.txt /app/
RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

COPY . /app/

CMD ["gunicorn", "--bind", ":8000", "dhost.wsgi"]

