sudo docker stop challenge001
sudo docker rm challenge001_old
sudo docker rename challenge001 challenge001_old
sudo docker build  -t v1/challenge001 .
sudo docker run -d -p 8000:8000 -e DATABASE_URL="postgis://ausanxyq:FMBkbmetG5XK7xaLEG_2ifU2Eo3WufVA@kesavan.db.elephantsql.com:5432/ausanxyq" --name challenge001 v1/challenge001
