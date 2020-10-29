FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
# COPY ./requirements.txt /var/www/requirements.txt
RUN pip install Flask
RUN pip install Flask_cors

WORKDIR /home/pizza

COPY backend/app.py .
COPY backend/pizza.py .
COPY backend/tweetBuilder.py .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]