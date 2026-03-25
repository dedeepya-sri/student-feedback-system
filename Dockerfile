FROM python:3.10

WORKDIR /app

COPY app/ /app/
COPY templates/ /app/templates/

RUN pip install flask

CMD ["python", "app.py"]