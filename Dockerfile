FROM python:3.7-buster

WORKDIR /home/jiggs
RUN useradd jiggs
COPY --chown=jiggs . /home/jiggs
RUN chown jiggs: /home/jiggs

USER jiggs

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "jiggs.py"]
