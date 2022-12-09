FROM python:3.8.5

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY projet/django/sentimentAnalysis/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]