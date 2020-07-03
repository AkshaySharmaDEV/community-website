FROM python:3.8.3-alpine

WORKDIR /app/api/

# prevents python from writing to pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# prevents python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .


COPY . .

ENTRYPOINT ["/app/api/entrypoint.sh"]