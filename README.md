# Scott's CS Notes :memo:

- :hammer: [Tools](#hammertools) [[Git](#git), [VSCode](#git)]
- :cloud: [Platform](#cloudplatform)[[GitHub](#github), AWS]
- :speech_balloon: [Languages](#languages) [Python, Java, C/C++]
- [Framework](#framework)[Flask]
- :computer: [Operating System](#operating-system) [Linux]
- :globe_with_meridians: [Network](#network)
- :floppy_disk: [Database](#database) [[SQL](#sql---structured-query-language), MongoDB]
- :bomb: [Resources](#resources) [[Rice MCS](#rice-mcs), [W3School](https://www.w3schools.com/), [CodeCademy](https://www.codecademy.com/)]
- :eyeglasses: [Interview Preparation](#interview-preparation) [[LeetCode](https://leetcode.com/)] 


## :hammer:Tools
### Git
- [Git Cheat Sheet - GitHub](https://education.github.com/git-cheat-sheet-education.pdf)
- [50 Git Commands - FreeCodeCamp](https://www.freecodecamp.org/news/git-cheat-sheet/)
### VSCode

## :cloud:Platform
### GitHub
#### Markdown
- [Emojis](https://gist.github.com/rxaviers/7360908)
- [Basic Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Languages

## Framework

## Operating System

## Network

## Database
### SQL - Structured Query Language
#### [W3S-SQL Tutorial](https://www.w3schools.com/sql/default.asp)
#### Subqueries
##### Non-Correlated Subqueries
```
SELECT * 
FROM flights 
WHERE origin in (
    SELECT code 
    FROM airports 
    WHERE elevation > 2000);
```
```
SELECT a.dep_month,
       a.dep_day_of_week,
       AVG(a.flight_count) AS average_flights
  FROM (
        SELECT dep_month,
              dep_day_of_week,
               dep_date,
               COUNT(*) AS flight_count
          FROM flights
         GROUP BY 1,2,3
       ) a
 GROUP BY 1,2
 ORDER BY 1,2;
```
##### Correlated Subqueries
A row is processed in the outer query.
Then, for that particular row in the outer query, the subquery is executed.
```
SELECT id
FROM flights AS f
WHERE distance > (
 SELECT AVG(distance)
 FROM flights
 WHERE carrier = f.carrier);
```
```
SELECT carrier, id,
    (SELECT COUNT(*)
FROM flights f
WHERE f.id < flights.id
AND f.carrier=flights.carrier) + 1
 AS flight_sequence_number
FROM flights;
```
#### Create Table
```
CREATE TABLE table_name(
    column_name1 datatype,
    column_name2 datatype,
    column_name3 datatype
);
```
#### Change Existing Table
##### Add Column to Table
```
ALTER TABLE table_name
ADD column_name datatype;
```

### MongoDB (No-SQL)

## Resources
### [Rice MCS](https://csweb.rice.edu/academics/graduate-programs/online-mcs)
- [x] COMP 614 (R): Python Programming [2022 Spring]
- [x] COMP 665 (S): Data Visualization [2022 Spring]
- [ ] **COMP 621 (E): Systems Software [2022 Fall]**
- [ ] **COMP 630 (R): Databases [2022 Fall]**
- [ ] **COMP 682 (R): Algorithms [2022 Fall]**
- [ ] COMP 643 (S): Big Data [2023 Spring]
- [ ] COMP 613 (R): Java Programming [2023 Spring]
- [ ] COMP 642 (E): Machine Learning [2023 Spring]
- [ ] COMP 610 (C): Software Construction [2023 Summer]

## Interview Preparation