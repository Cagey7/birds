FROM python:3.8-alpine

RUN apk update && apk add bash
RUN apk add --no-cache bash

WORKDIR /birds
COPY . /birds

RUN pip install -r requirements.txt

EXPOSE 5000 5001

CMD ["./boot.sh"]
