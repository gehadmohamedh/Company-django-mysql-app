FROM python:3.10.12

RUN pip install --upgrade pip

ENV DATABASE_OWNER "defualt_user"

RUN mkdir /app

COPY requierments.txt /app/

WORKDIR /app

RUN pip install -r requierments.txt

COPY radrodaProject .

EXPOSE 8000
WORKDIR /app/

ENV DB_NAME="django"
ENV DB_USER="django"
ENV DB_PASS="123456789"
ENV HOST_IP="172.17.0.1"

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000