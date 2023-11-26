FROM python:3.11.6-alpine3.17

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "192.168.0.1", "--port", "8080"]

#docker run -d --name mycontainer -p 80:80 myimage