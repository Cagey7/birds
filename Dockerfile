FROM python:3.8-alpine

WORKDIR /birds
COPY . /birds

RUN pip install -r requirements.txt

CMD ["python", "birds.py"]
