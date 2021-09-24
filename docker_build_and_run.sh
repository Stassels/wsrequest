docker build ./ -t wsrequest
docker run --name wsrequest -p 8000:8000 wsrequest
