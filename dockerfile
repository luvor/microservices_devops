FROM python:3.10-slim-buster

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app

COPY common/ /app/common/
COPY models/ /app/models/
COPY complete_users_service.py /app/
COPY get_users_service.py /app/
COPY insert_users_service.py /app/
COPY notify_users_service.py /app/

CMD ["python", "complete_users_service.py"]
