FROM debian:stable-slim

ENV PORT=8991

# COPY source destination
COPY learning-docker /bin/learning-docker

CMD ["/bin/learning-docker"]