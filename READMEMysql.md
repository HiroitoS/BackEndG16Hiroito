SQL LESSON 1
 1. SELECT title FROM movies;
 2. SELECT director FROM movies;
 3. SELECT title, director FROM movies;
 4. SELECT title, year FROM movies;
 5. SELECT * FROM movies;
----------------------------------------------
SQL LESSON 2
1.  SELECT * FROM movies WHERE id = 6;
2.  SELECT * FROM movies WHERE year BETWEEN 2000 AND 2010;
3.  SELECT * FROM movies WHERE year NOT BETWEEN 2000 AND 2010;
4.  SELECT title, year FROM movies WHERE id BETWEEN 1 AND 5;
-----------------------------------------------------------------------------------------------------
SQL LESSON 3 PARTE 1
1.  SELECT * FROM movies WHERE title LIKE "toy %";
2.  SELECT * FROM movies WHERE Director LIKE "John%";
3.  SELECT * FROM movies WHERE Director NOT LIKE "John%"
4.  SELECT * FROM movies WHERE title LIKE "WALL-%";
-----------------------------------------------------------------------------------------------------
REPASO

1.  SELECT DISTINCT director FROM movies ORDER BY director asc;
2.  SELECT * FROM movies ORDER BY year desc LIMIT 4;
3.  SELECT * FROM movies ORDER BY title LIMIT 5;
4.  SELECT * FROM movies ORDER BY title LIMIT 5 OFFSET 5;

-----------------------------------------------------------------------------------------------------
SQL LESSON 3 PARTE 2
1.  SELECT * FROM North_american_cities WHERE country = "Canada";
2.  SELECT country, city, latitude FROM North_american_cities WHERE Country = "United States" ORDER BY latitude desc;
3.  SELECT city, longitude FROM north_american_cities WHERE longitude < -87.629798 ORDER BY longitude ASC;
4.  SELECT country, city, population FROM North_american_cities WHERE country = "Mexico" ORDER BY population DESC LIMIT 2
5.  SELECT country, city, population FROM North_american_cities WHERE country = "United States" ORDER BY population DESC LIMIT 2 OFFSET 2;
----------------------------------------------------------------------------------------------------

