Welcome to the interview!

Table input
id	date	transaction
1	2019-10-02	10
2	2019-10-05	89
3	2019-10-07	101
4	2019-10-11	45
5	2019-11-02	201
6	2019-11-03	321
7	2019-11-05	1890
8	2019-12-01	320

Id and date always increase and either id or date can be used as the primary key of the table. Find the days (or ids) with transaction amount equal or above 100 for
at least 3 consecutive record. In this table, id=6,8,10,12 are transactions over the 100 and are consecutive. Thus, the output table shall be

SELECT id FROM Input WHERE Transaction > 100

id	date	transaction rank diff
3	2019-10-07	101 1 2
5	2019-11-02	201 2 3
6	2019-11-03	321 3 3
7	2019-11-05	1890 4 3
8	2019-12-01	320 5 3
