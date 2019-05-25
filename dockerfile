FROM python:3.7

RUN pip3 install pipenv gunicorn

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

ADD . .

EXPOSE 80

#RUN pytest

CMD [ "gunicorn", "-b0.0.0.0:80", "wsgi:app" ]