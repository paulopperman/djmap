#djmap
Testing and experimenting with a dockerized GeoDjango setup. The main purpose of this is to get around dependency 
conflicts on the host system.

* Initial commit implements the [GeoDjango tutorial](https://docs.djangoproject.com/en/1.11/ref/contrib/gis/tutorial/)
   * To use the shell effectively, run `sudo docker exec -i -t <container_name>` and do the shell stuff

## Notes
* The additional packages on the python image were added out of abundance of caution.  They may not be necessary, but it
hasn't been tested.  