FROM nginx:latest

COPY simple_flask.conf /etc/nginx/conf.d/simple_flask.conf
RUN rm -rf /etc/nginx/conf.d/default
RUN rm -rf /etc/nginx/conf.d/default.conf
RUN service nginx restart

