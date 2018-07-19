#GCP Stop & Start 

Script desarrollado para el auto apagado y encendido de instancias de tipo Compute Engine en GCP

### Pre-Requisites

* Install the gcloud CLI from https://cloud.google.com/sdk 
* Install the Python client library for Google APIs by running `pip install --upgrade google-api-python-client`


### Deployment

* Get a local copy of the git project
* Execute the python scripts as follow:

./gcp-shst.py -p {project - ex: myproject} -z {project's zone -ex: southamerica-east1-a} -i {instance name - ex: my-instance} -o {operation - ex: start}

* Crontab
 
Schedule the scripts as a crontab task:

** Edit crontab 
# crontab -e
** Configure as desired
# stop at night
0 22 * * * /{python path} /{path}/gcp-shst.py -p myproject -z southamerica-east1-a -i myinstance -o stop
# start when getting up
0 8  * * * /{python path} /{path}/gcp-shst.py -p myproject -z southamerica-east1-a -i myinstance -o start
