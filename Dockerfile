FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pytest requests

CMD ["pytest"]