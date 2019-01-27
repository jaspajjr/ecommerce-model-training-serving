FROM python:3.6

COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry
RUN mkdir /results
RUN chmod 0755 /results

RUN useradd -ms /bin/bash defaultUser && adduser defaultUser sudo

COPY requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt

USER defaultUser
CMD ["start"]
ENTRYPOINT [ "/entry" ]

COPY serving_app /data