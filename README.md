# PyMongo stater code

## Anaconda setup

```bash
conda create --name mongo
source activate mongo
pip install pymongo==3.1.1
```

## MongoDB docker

### Start MongoDB

Currently data is not persisted

```bash
./start_mongo.sh

or

docker run -d -p 27017:27017 --name mongo -d mongo
```

### Check logs

```bash
 docker logs -f mongo
 ```

## Run mongo db client

 ```bash
 python sample.py
 ```

## References

- [MongoDB tutorial](http://api.mongodb.com/python/current/tutorial.html)