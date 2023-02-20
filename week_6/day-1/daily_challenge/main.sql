-- create a table
CREATE TABLE actors (
  actor_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age date NOT NULL,
  number_oscars INTEGER,
);
-- insert some values
INSERT INTO actors VALUES (1, 'Matt', 'Demon', 1970-08-10, 5);
INSERT INTO actors VALUES (2, 'Jeniffer', 'Aniston', 1969-02-11, 0);
INSERT INTO actors VALUES (3, 'George', 'Clooney', 1961-06-04, 2);
INSERT INTO actors VALUES (4, 'Angelina', 'jolie', 1975-06-04, 2);
INSERT INTO actors VALUES (5, 'Tom', 'Cruise', 1962-07-03, 0);
INSERT INTO actors VALUES (6, 'Will', 'Smith', 1968-09-25, 0);
INSERT INTO actors VALUES (7, 'Kevin', 'Hart', 1979-07-06, 0);
-- fetch some values

SELECT COUNT(*) FROM actors;