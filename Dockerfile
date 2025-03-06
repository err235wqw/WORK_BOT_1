FROM python:3.13-slim
WORKDIR /server_tgbot
ADD . '/server_tgbot/'
RUN pip install -r requirements.txt
CMD ["python", "run.py"]