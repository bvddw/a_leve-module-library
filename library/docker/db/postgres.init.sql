/* put database initialization script here */

-- for example
CREATE ROLE ladmin WITH ENCRYPTED PASSWORD 'password' LOGIN;
COMMENT ON ROLE ladmin IS 'docker user for tests';

CREATE DATABASE ldb OWNER ladmin;
COMMENT ON DATABASE ldb IS 'docker db for tests owned by docker user';
