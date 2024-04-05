# Parallel Gateway Network and MQTT Demo

This repository is used as a development stack to demonstrate utilizing MQTT to reduce the load on the Gateway Network

# How It Works

* Tag data (realtime and historical) utilizes MQTT to get information between gateways
* Enterprise Administration Module (EAM), Alarm event data, and Audit logs communicate over the Gateway Network

# Setup

* Clone Git Repo
* Open dir in your IDE of choice
* Run ` "docker compose up -d" `
* gw username ` admin `
* gw passwords ` password `

# Gateway Info

corpGateway ` localhost:8089 `
* Approve Certificate In Incoming GWN connection from siteGateway
* Approve Incoming connection More > Approve

siteGateway ` localhost:8090 `
* Approve Certificate In Incoming GWN connection from 
* Approve Incoming connection More > Approve

edgeGateway ` localhost:8091 `
