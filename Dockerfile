FROM python:3
ADD  bot.py /
ADD .env /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "bot.py" ]
