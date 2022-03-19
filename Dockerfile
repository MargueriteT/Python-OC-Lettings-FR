FROM python:3.8

WORKDIR /oc_lettings_site

ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV DEBUG=True

ADD . /oc_lettings_site

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /oc_lettings_site

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]