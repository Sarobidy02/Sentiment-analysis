FROM python:3.8.5

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install pandas
RUN pip install -U scikit-learn

EXPOSE 8000