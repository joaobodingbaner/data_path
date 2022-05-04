CREATE database datapath;

CREATE SCHEMA aulademo;

CREATE TABLE [IF NOT EXISTS] aulademo.tb_bitcoin_trades_buy (
   id serial PRIMARY KEY,
   date_trade TIMESTAMP,
   amount float(7),
   price INT,
   tid INT,
   type_trade VARCHAR(4)
);

