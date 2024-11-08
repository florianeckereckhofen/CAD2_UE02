# Cloud Architecture Design 2 Übung 2

Ziel: Eine einfache Voting-App die mehrere Services integriert wie eine Web-Anwendung, eine Redis-Datenbank, einen Worker und eine PostgreSQL-Datenbank. Diese Architektur stellt sicher, dass Daten persistent gespeichert werden und verschiedene Teile der Anwendung in unterschiedlichen Containern laufen.

Komponenten:
•	Voting-WebApp: Geschrieben in Python und Node.js. Die Komponente ermöglicht es abzustimmen.
•	Redis-Container: In-Memory-Datenbank für schnelle Speicherung der Ergebnisse.
•	Worker-Container: Sammelt Daten aus Redis und schreibt sie in die PostgreSQL-Datenbank.
•	PostgreSQL-Container: Für die persistente Speicherung der gesammelten Daten.
•	Result-App: Eine Web-App, die die gespeicherten Abstimmungsergebnisse anzeigt.

1.	Dockerfiles erstellen: Voting-App, Worker und Result-App.
2.	Docker Compose Datei erstellen für die orchestrierung.
3.	docker-compose up --build
  a.	IP für Voting-App: http://127.0.0.1:5000/
  b.	IP für Result-App: http://127.0.0.1:5001/

Zusätzlich muss noch vor dem Start in der SQL Datenbank der votes Table erstellt werden: 
1.	docker-compose exec db psql -U postgres
2.	CREATE TABLE votes ( id SERIAL PRIMARY KEY, vote VARCHAR(50) );
3.	docker-compose up --build

