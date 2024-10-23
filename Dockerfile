FROM python:3.12-slim

WORKDIR /opt/server

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "metanit/manage.py", "runserver", "0.0.0.0:5000" ]

