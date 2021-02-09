FROM python:3.9

EXPOSE 8000
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--bind", ":8000", "dhost.wsgi"]

