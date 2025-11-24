FROM python:3.13

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./flask_project .

COPY ./gunicorn.conf.py .

EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
