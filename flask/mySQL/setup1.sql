use mydb;
INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'Washington', 'WA');
INSERT into Cities (create_time, update_time, name, States_id) values (now(), now(), 'Seattle',1);
INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'Safeway', 'various');

INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'Idaho', 'ID');
INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'Oregon', 'OR');
INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'California', 'CA');
INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'Alaska', 'AK');
INSERT into States (create_time, update_time, name, abbreviation) values (now(), now(), 'Delaware', 'DE');
INSERT into Cities (create_time, update_time, name, States_id) values (now(), now(), 'Moses Lake',1);
INSERT into Cities (create_time, update_time, name, States_id) values (now(), now(), 'Darrington',1);
INSERT into Cities (create_time, update_time, name, States_id) values (now(), now(), 'Everett',1);
INSERT into Cities (create_time, update_time, name, States_id) values (now(), now(), 'Tacoma',1);

INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'Tullys', 'Patrick Dempsey');
INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'Starbucks', 'Howard Schultz');
INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'Coding Dojo', 'Michael Choi');
INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'Joes Garage', 'Joe');
INSERT into Businesses (create_time, update_time, name, owner) values (now(), now(), 'US Bank', 'Who knows');

DELETE from States where id=2;
DELETE from Cities where id=2;
DELETE from Businesses where id=2;
