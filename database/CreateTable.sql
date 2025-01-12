create table Player (
	PlayerID char(50),
    Skill long,
    NumGames int,
    AbandonedGames int,
    Rank1 int,
    Rank2 int,
    Rank3 int,
    Rank4 int,
    CreationDate timestamp
);

create table Identity (
	PlayerID char(50),
    Passcode char(50)
);

create table PlayerHistory (
	PlayerID char(50),
    HistoryDate date,
    Skill long,
    NumGames int,
    AbandonedGames int,
    Rank1 int,
    Rank2 int,
    Rank3 int,
    Rank4 int
);