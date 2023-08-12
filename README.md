# linkserver

A directory of links, configurable entirely by environment variables.

e.g. with docker-compose you can do the following:

```yaml
linkserver:
    image: ----
    environment:
        SONARR: https://192.168.2.200:3423
        RADARR: https://192.168.2.200:3423
        JACKETT: https://192.168.2.200:3423
``` 

It should also incrementally check to grab the favicons from the services and their given URLs.
