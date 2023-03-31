-- a script that lists all records of the table second_table of the database
-- The database name will be passed as an argument to
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
