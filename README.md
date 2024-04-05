Description:
	Tag realtime and history communicating over MQTT. EAM, Alarm Event, Audit, communicating over GWN.

Setup:

Clone Git Repo
Open dir in IDE
run "docker compose up -d"
gw usernames: admin
gw passwords: password

corpGateway: localhost:8089
	Approve Certificate In Incoming GWN connection from siteGateway
	Approve Incoming connection More►Approve

siteGateway: localhost:8090
	Approve Certificate In Incoming GWN connection from 
	Approve Incoming connection More►Approve

edgeGateway: localhost:8091