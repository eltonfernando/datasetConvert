CREATE TABLE "anotation" (
	"name_image"	TEXT NOT NULL,
	"size_image"	TEXT,
	PRIMARY KEY("name_image")
);

CREATE TABLE "bandbox" (
	"id"	TEXT,
	"box"	TEXT NOT NULL,
	FOREIGN KEY("id") REFERENCES "anotation"("name_image")
);

CREATE TABLE "images" (
	"id"	TEXT,
	"bytes_image"	BLOB,
	FOREIGN KEY("id") REFERENCES "anotation"("name_image")
);

CREATE TABLE "segmentation" (
	"id"	TEXT,
	"point"	TEXT,
	FOREIGN KEY("id") REFERENCES "anotation"("name_image")
);