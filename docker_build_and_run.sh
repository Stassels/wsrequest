docker build ./ -t wsrequest
docker run --name wsrequest -d -p 8000:8000 wsrequest
