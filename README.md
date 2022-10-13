# Scott's CS Notes :memo:
test
- :hammer: [Tools](#hammertools) [[Git](#git), [VSCode](#git)]
- :cloud: [Platform](#cloudplatform)[[GitHub](#github), AWS]
- :speech_balloon: [Languages](#languages) [Python, Java, C/C++]
- [Framework](#framework)[Flask]
- :computer: [Operating System](#operating-system) [Linux]
- :globe_with_meridians: [Network](#network) [[AWS](http://aws.amazon.com)]
- :floppy_disk: [Database](#database) [[SQL](#sql---structured-query-language), MongoDB]
- :bomb: [Resources](#resources) [[Rice MCS](#rice-mcs), [W3School](https://www.w3schools.com/), [CodeCademy](https://www.codecademy.com/)]
- :eyeglasses: [Interview Preparation](#interview-preparation) [[LeetCode](https://leetcode.com/), [NeetCode](https://neetcode.io/)] 


## :hammer:Tools
### Git
- [Git Cheat Sheet - GitHub](https://education.github.com/git-cheat-sheet-education.pdf)
- [50 Git Commands - FreeCodeCamp](https://www.freecodecamp.org/news/git-cheat-sheet/)
### VSCode
### [CodeSkulptor](https://py3.codeskulptor.org/) - browser based collaborative Python3 IDE
## :cloud:Platform
### GitHub
#### Markdown
- [Emojis](https://gist.github.com/rxaviers/7360908)
- [Basic Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## Languages

## Framework

## Operating System

## Network
### AWS
EC2
t2.micro
Free tier: In your first year includes 750 hours of t2.micro (or t3.micro in the Regions in which t2.micro is unavailable) instance usage on free tier AMIs per month, 30 GiB of EBS storage, 2 million IOs, 1 GB of snapshots, and 100 GB of bandwidth to the internet.
## Database
### SQL - Structured Query Language
#### [W3S-SQL Tutorial](https://www.w3schools.com/sql/default.asp)
#### [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
#### Subqueries
##### Non-Correlated Subqueries
```sql
SELECT * 
FROM flights 
WHERE origin in (
    SELECT code 
    FROM airports 
    WHERE elevation > 2000);
```
```sql
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
```sql
SELECT id
FROM flights AS f
WHERE distance > (
 SELECT AVG(distance)
 FROM flights
 WHERE carrier = f.carrier);
```
```sql
SELECT carrier, id,
    (SELECT COUNT(*)
FROM flights f
WHERE f.id < flights.id
AND f.carrier=flights.carrier) + 1
 AS flight_sequence_number
FROM flights;
```
#### Create Table
```sql
CREATE TABLE table_name(
    column_name1 datatype,
    column_name2 datatype,
    column_name3 datatype
);
```
#### Change Existing Table
##### Add Column to Table
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

### MongoDB (No-SQL)

## Resources
### [Rice MCS](https://csweb.rice.edu/academics/graduate-programs/online-mcs)
- [x] COMP 614 (R): Python Programming [2022 Spring]
- [x] COMP 665 (S): Data Visualization [2022 Spring]
- [ ] [**COMP 630 (R): Databases [2022 Fall] [THU 6:30PM]**](RiceMCS/COMP630_Databases.md)
- [ ] [**COMP 682 (R): Algorithms [2022 Fall] [THU 8:00PM]**](RiceMCS/COMP682_Algorithms.md)
- [ ] [**COMP 643 (S): Big Data [2022 Fall] [WED 6:30PM]**](RiceMCS/COMP643_BigData.md)
- [ ] [**COMP 628 (S): Cyber Security [2022 Fall] [TUE 6:30PM]**](RiceMCS/COMP628_CyberSecurity.md)
- [ ] COMP 621 (E): Systems Software [2023 Spring]
- [ ] COMP 613 (R): Java Programming [2023 Spring]
- [ ] COMP 642 (E): Machine Learning [2023 Spring]
- [ ] COMP 610 (C): Software Construction [2022 Spring]

## Interview Preparation
### [LeetCode - Blind 75](LeetCodeBlind75.md)
