sudo docker stop wsrequest
sudo docker build ./ -t wsrequest
sudo docker run --name wsrequest -d -p 8000:8000 wsrequest
