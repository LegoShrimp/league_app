drop table if exists champions;
drop table if exists game;
drop table if exists champ_game
create table champions ( 
	id integer primary key,
    role text,
	name text,
	win integer,
	loss integer,
    total integer

);
create table champ_game (
    gameid integer primary key,
    --team 1 blue
    champ1 integer,
    champ2 integer,
    champ3 integer,
    champ4 integer,
    champ5 integer,
    --team 2 red
    champ6 integer,
    champ7 integer,
    champ8 integer,
    champ9 integer,
    champ10 integer,
    win boolean --0 team 1 win, 1 team 2 win
    );
     
