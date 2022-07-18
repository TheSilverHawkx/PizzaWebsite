DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Users(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	username TEXT UNIQUE NOT NULL,
  	displayName TEXT NOT NULL,
  	password TEXT NOT NULL,
    type TEXT CHECK( type in ('customer','employee','admin')) NOT NULL DEFAULT 'customer'
  ) ;

CREATE TABLE IF NOT EXISTS Products(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	name TEXT UNIQUE NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    type TEXT CHECK( type in ('pizza','topping','dough', 'sauce')) NOT NULL
  ) ;

CREATE TABLE IF NOT EXISTS Orders(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	customerId INTEGER NOT NULL,
    configuration TEXT NOT NULL,
    address TEXT NOT NULL
  ) ;