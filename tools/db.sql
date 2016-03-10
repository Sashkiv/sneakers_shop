CREATE DATABASE shop_db ENCODING 'utf-8';
CREATE USER shop_user WITH PASSWORD 'evYB5rKkxcNcQN8TnEpW';
GRANT ALL PRIVILEGES ON database shop_db TO shop_user;
ALTER DATABASE shop_db OWNER TO shop_user;

CREATE DATABASE test_shop_db ENCODING 'utf-8';
CREATE USER test_shop_user WITH PASSWORD 'FWynCrbLPH5DTKD';
GRANT ALL PRIVILEGES ON database test_shop_db TO test_shop_user;
ALTER DATABASE test_shop_db OWNER TO test_shop_user;
ALTER USER test_shop_user CREATEDB;
