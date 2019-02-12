FROM nginx:alpine

ENV APP_DIR /app
ENV TZ=Europe/Berlin
RUN mkdir -p ${APP_DIR}

RUN apk add --no-cache python3 uwsgi uwsgi-python3 iputils

COPY frontend_server/requirements.txt ${APP_DIR}/

RUN apk add --no-cache --virtual build-dependencies \
       gcc \
       python3-dev \
       musl-dev \
       linux-headers \
       git \
       openssh \
       tzdata \
       && cp /usr/share/zoneinfo/$TZ /etc/localtime \
       && echo $TZ > /etc/timezone \
       && pip3 install -r ${APP_DIR}/server-requirements.txt \
       && apk del build-dependencies \
       && rm -rf /var/lib/apt/lists/*

COPY deploy/frontend/nginx.conf /etc/nginx/conf.d/default.conf
COPY deploy/frontend/uwsgi.ini frontend_server/application.py ${APP_DIR}/
COPY frontend_server/app_server ${APP_DIR}/app_server
CMD nginx && uwsgi --ini ${APP_DIR}/uwsgi.ini --lazy-apps