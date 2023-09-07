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


ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASS=${DB_PASS}
ENV HOST_IP="localhost"

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000