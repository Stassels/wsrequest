FROM python:3.6-slim-buster
# Copy source files
COPY . .
# Install our deps
RUN python -m pip install -U pip
RUN pip3 install -r requirements.txt
## Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "app:server"]

