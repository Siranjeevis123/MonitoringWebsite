FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5001

CMD ["flask", "run"]

give me the more details about running files 
wifi status and speed
current time and date at the top
like fully funtional ui
mac version and space free memory
curently what i am using that details
