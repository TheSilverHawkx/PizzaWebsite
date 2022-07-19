DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Orders;

CREATE TABLE IF NOT EXISTS Users(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	username TEXT UNIQUE NOT NULL,
  	displayName TEXT NOT NULL,
  	password TEXT NOT NULL,
    type TEXT CHECK( type in ('Customer','Employee','Admin')) NOT NULL DEFAULT 'Customer'
  ) ;

CREATE TABLE IF NOT EXISTS Products(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	name TEXT UNIQUE NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    type TEXT CHECK( type in ('Topping','Dough', 'Sauce','Cheese')) NOT NULL
  ) ;

CREATE TABLE IF NOT EXISTS Orders(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
    creationDate timestamp NOT NULL,
  	customerId INTEGER NOT NULL,
    configuration TEXT NOT NULL,
    address TEXT NOT NULL,
    status TEXT CHECK(status in ('New','InProgress','Done')) NOT NULL DEFAULT 'New'
  ) ;