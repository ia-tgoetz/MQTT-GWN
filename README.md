# Parallel Gateway Network and MQTT Demo

This repository is used as a development stack to demonstrate utilizing MQTT to reduce the load on the Gateway Network

# How It Works

* Tag data (realtime and historical) utilizes MQTT to get information between gateways.
* MQTT Transmission's Store and Forward Buffer is used to ensure Data is not lost between the Edge and Site Gateways.
* Enterprise Administration Module (EAM), Alarm event data, Alarm Journal, and Audit logs communicate over the Gateway Network

<p align="center">
  <img src="https://github.com/ia-tgoetz/MQTT-GWN/blob/main/GWNMQTTArch.JPG?raw=true" alt="alt text">
</p>

# Setup
* Clone Git Repo
* Open dir in your IDE of choice
* Run ` "docker compose up -d" `
* gw username ` admin `
* gw passwords ` password `

# Gateway Info

corpGateway ` localhost:8089 `
* Delete All Certificates and Incoming connections
* Approve Certificate In Incoming GWN connection from siteGateway
* Approve Incoming connection More > Approve

siteGateway ` localhost:8090 `
* Delete All Certificates and Incoming connections
* Approve Certificate In Incoming GWN connection from 
* Approve Incoming connection More > Approve

edgeGateway ` localhost:8091 `

# Resources
* Better Understand MQTT and MQTT Transmission with this [Video Series](https://inductiveautomation.com/resources/video/what-is-mqtt)
* Configure Edge [Sync Services](https://docs.inductiveautomation.com/docs/8.1/other-editions/ignition-edge/edge-gateway/configuring-sync-services) 
