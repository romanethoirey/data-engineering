FROM python:3.7

USER root
WORKDIR /home

COPY requirements.txt .

ENV FLASK_APP=app.py

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]