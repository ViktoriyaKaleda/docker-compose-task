FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x migrate.sh
CMD ["sh", "-c", "./migrate.sh; python server.py"]
