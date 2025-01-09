# Database Structure for Player application

Player table:

```
playerId (50 chars) - primary key
skill (long)
numberGames (int)
abandonedGames (int)
rank1 (int)
rank2 (int)
rank3 (int)
rank4 (int)
creationDate (timestamp)
```

Identity table:

```
playerId (50 chars) - foreign key
password (50 chars)
```

Player_history table:

```
playerId (50 chars) - foreign key
historyDate (date) - secondary key
skill (long)
numberGames (int)
abandonedGames (int)
rank1 (int)
rank2 (int)
rank3 (int)
rank4 (int)
```
