FROM python:3.10
WORKDIR /app
COPY . .
RUN  apt install openssl \
#&& python -m virtualenv env \
#&& source /app/env/bin/activate \
&& pip install -r requirements 
CMD ["/app/startup.sh"]
