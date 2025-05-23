# Application for Player REST API interface

Repository content:

- Database structure and initialization: [database/README.md](database/README.md)
- Source code [python/README.md](python/README.md)
- Kubernetes artifacts [k8s/README.md](k8s/README.md)

API detail:

- `GET /player` - list playerIds

- `POST /player` - create a new Player - error if duplicate playerID - error if playerID invalid - error if data is invalid

- `GET /player/{playerID}` - get a Specific player - 404 if playerID not found

- `POST /player/{playerID}` - update a player's password - error if duplicate playerID - error if playerID invalid - error if data is invalid

- `PATCH /player/{playerID}` - update a player - 404 if playerID not found; 500 if update data invalid

- `DELETE /player/{playerID}` - delete a player - 404 if playerID not found