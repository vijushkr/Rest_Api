FROM ubuntu:18.04

# Update apt packages
RUN apt update
RUN apt upgrade -y

# Install vim
RUN apt install vim -y



# Install python 3.7
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.7 -y

# Make python 3.7 the default
RUN echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN /bin/bash -c "source ~/.bashrc"

# Install pip
RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

#install mongodb
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu/ xenial/mongodb-org/3.4 multiverse" |  tee /etc/apt/sources.list.d/mongodb-3.4.list

RUN apt-get update && apt-get install -y mongodb
RUN mkdir -p /data/db
RUN chown -R mongodb:mongodb /data/db
ADD var/lib/mongodb/mongodb.conf /etc/mongodb.conf
ADD mongodb.pem /etc/ssl/certs/mongodb.pem

VOLUME ["/data/db"]
EXPOSE 27017
ENTRYPOINT ["/usr/bin/mongod", "--config", "/etc/mongodb.conf"]

# install Python modules needed by the Python app
COPY requirement.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirement.txt

# copy files required for the app to run
COPY DjangoRestApiMongoDB  /usr/src/app/

COPY mywebApp  /usr/src/app/

COPY manage.py  /usr/src/app/


# tell the port number the container should expose
EXPOSE 8000

# run the application

CMD ["python", "/usr/src/app/manage.py migrate"]
CMD ["python", "/usr/src/app/manage.py runserver"]
