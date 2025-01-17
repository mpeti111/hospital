BEGIN;

CREATE TABLE Roles(
	id SERIAL PRIMARY KEY,
	role INTEGER CHECK (role IN (1, 2))
);
INSERT INTO Roles (role) VALUES (1), (2);

CREATE TABLE Users (
id SERIAL PRIMARY KEY,
	Name VARCHAR(50),
	LastName VARCHAR(50),
	Phone VARCHAR(17),
	Login VARCHAR(50),
	Password VARCHAR(50),
	Role INTEGER DEFAULT 2 REFERENCES Roles(id)
);
COMMIT;