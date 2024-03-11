FROM python:3.8.18-bullseye

WORKDIR /app

RUN apt update
RUN apt install git
RUN git clone https://github.com/TimWelter/sellix_discord_bot.git .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
