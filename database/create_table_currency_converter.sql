CREATE TABLE currency_converter
(
ID int NOT NULL AUTO_INCREMENT,
on_date date,
from_currency varchar(32),
to_currency varchar(32),
rate float(10,5),
PRIMARY KEY (Id)
);
