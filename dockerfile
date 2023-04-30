FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "reset-collections.py"]