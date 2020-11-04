FROM python:3.7-stretch
WORKDIR /opt
COPY pronsearch/requirements.txt /opt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install cron -y
COPY pronsearch/ /opt
CMD [ "python","runserver.py" ]
EXPOSE 7789