-- Database: template

-- DROP DATABASE template;

CREATE DATABASE template
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE template TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE template TO PUBLIC;

GRANT ALL ON DATABASE template TO template;