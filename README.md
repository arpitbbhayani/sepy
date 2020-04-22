# sepy

sepy is a very "Search Engine written in Python" to be used for education.

To build your search engine you need to complete part_01 to part_10. Each of the segments
has a function that represents one important piece in your search engine.
You can visualize the results using a web frontend [sepy-fr](https://github.com/arpitbbhayani/sepy-fr).

## Requirements

```
python3.7
```

## Setting up Virtualenv

```
virtualenv venv -p `which python3.7`
. venv/bin/activate
```

## Installing packages
```
pip install -r requirements.txt
```

## Linting
```
pylint sepy
```

## Running

```
python run.py --datasetdir ~/data/datasets
```

## Datasets

 - [Harry Potter Dataset (15298 documents)](https://drive.google.com/open?id=1zsAW8PUNVxpZ_F5Yk1zi-AT7cfkG3nkK)
 - [Harry Potter Dataset Subset (1000 documents)](https://drive.google.com/open?id=1ky5RExEjwBdP3NvOvdj2aZTHAANQXhia)
