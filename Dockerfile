FROM python:3.10-slim

WORKDIR /service

RUN apt-get update && apt-get install -y

COPY ./requirements.txt .

RUN pip install --no-cache --upgrade -r requirements.txt

COPY ./.env .
COPY ./pyproject.toml .

EXPOSE 8000

CMD ["python3", "-m", "src.main"]