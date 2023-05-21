FROM python:3.8
RUN mkdir /code
COPY . /code/
RUN apt-get update
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 80
WORKDIR /code/
CMD ["python", "./app.py"]