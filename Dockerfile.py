# Build from a slim Debian/Linux image
FROM debian:stable-slim

# Update apt and upgrade packages
RUN apt update && apt upgrade -y

# Install Python 3
RUN apt install -y python3

COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]