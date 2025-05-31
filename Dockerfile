FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=password

ENV MYSQL_USER=user

EXPOSE 3306

COPY init.sql /docker-entrypoint-initdb.d/ 

CMD ["mysqld"]