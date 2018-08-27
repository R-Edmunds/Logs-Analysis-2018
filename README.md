# Logs Analysis project - Robin Edmunds 2018

## Environment

Development environment is an __Ubuntu 18.04__ host running __Vagrant/libvirt__ with
__debian/jessie64__ box.

### Versions
- psql 9.4.18
- Python 3.4.2
- pip3 18
- psycopg2 2.5.4
- git version 2.1.4

## SQL View definitions
```sql
CREATE VIEW view_daily_errors AS
    -- return total request errors for each day
    SELECT subq_errors.date, COUNT(subq_errors.date) AS daily_errors
    FROM
        (SELECT CAST(log.time AS DATE) AS date
        FROM log
        WHERE log.status != '200 OK') AS subq_errors
    GROUP BY subq_errors.date
    ORDER BY subq_errors.date;

CREATE VIEW view_daily_requests AS
    -- return total requests for each day
    SELECT subq_daily_requests.date, COUNT(subq_daily_requests.date) AS daily_requests
    FROM
        (SELECT CAST(log.time AS DATE) AS date
        FROM log) AS subq_daily_requests
    GROUP BY subq_daily_requests.date
    ORDER BY subq_daily_requests.date;
    ```
