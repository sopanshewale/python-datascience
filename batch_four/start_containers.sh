#!/bin/sh

echo 'Starting Containers for jupyter service'
docker run -d -p 8888:8888 --name jupyter -v /Users/sopanshewale/datascience/aegis/python-datascience/batch_four/jupyter:/app  -t batchfour_jupyter /bin/bash
