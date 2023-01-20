
FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . .
# RUN python manage.py collectstatic --noinput
CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "core.wsgi" ]