FROM python:3.7-buster

WORKDIR /home/jiggs
RUN useradd jiggs

COPY --chown=jiggs . /home/jiggs
RUN chown -R jiggs: /home/jiggs

ENV PATH="/home/jiggs/.local/bin:${PATH}"

USER jiggs

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "jiggs.py"]
