FROM ubuntu:18.04
RUN apt-get update \
    && apt install -y --no-install-recommends curl \
    && apt-get install -y --no-install-recommends python
WORKDIR /
COPY . .
RUN ls -lrt
ENTRYPOINT ["python", "webapp.py"]