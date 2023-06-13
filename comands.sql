
-- CREATE TABLE persona (
-- 	id serial PRIMARY KEY,
-- 	name VARCHAR (50) NOT NULL,
-- 	last_name VARCHAR (50) NOT NULL,
-- 	email VARCHAR (150)
-- );

-- CREATE TABLE departamento (
-- 	id serial PRIMARY KEY,
-- 	name VARCHAR (50) NOT NULL,
-- 	fk_persona integer,
-- 	CONSTRAINT depto_frkey FOREIGN KEY (fk_persona) 
-- 	REFERENCES persona (id)
-- );

alter table persona add column depto_fk int;                -- AGREGAR UNA COLUMNA A LA TABLA
alter table persona add CONSTRAINT persona_frkey FOREIGN key (depto_fk) references departamento (id)  -- una relación entre la tabla "persona" y la tabla "departamento" utilizando la columna "id" como clave externa.
update persona set depto_fk = valor where id = valor;     -- AGREGAR UN VALOR A LA COLUMNA DEPTO_FK        
alter table persona alter column depto_fk set not null;      -- ACTUALIZA LA COLUMNA PARA CUANDO SE CARGA NO SEA NULL

INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');         -- CARGAR UNA PERSONA
INSERT INTO departamento (name, fk_persona) values ('compras', 1);         -- CARGAR UN DEPARTAMENTO

SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;

DELETE FROM persona WHERE id = 2;

UPDATE persona SET email = 'algo@algo.com' WHERE id = 15;           

select * from departamento d join persona p on (d.fk_persona = p.id) where p.id =1;