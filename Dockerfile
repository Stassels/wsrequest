FROM python:2.7
# Copy source files
COPY . .
# Install our deps
RUN python -m pip install -U pip
RUN pip install -r requirements.txt
## Finally, run gunicorn.
CMD [ "gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:8000", "app:server"]

