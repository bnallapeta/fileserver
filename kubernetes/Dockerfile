FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ../server/fileserver ./
COPY ./entry.sh ./

COPY ../server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["./entry.sh" ]