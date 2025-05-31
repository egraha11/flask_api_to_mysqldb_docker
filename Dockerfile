FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip
#RUN apt install python3

RUN pip3 install --break-system-packages -r requirements.txt

EXPOSE 25565:25565

CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["python3", "flask_api.py"]