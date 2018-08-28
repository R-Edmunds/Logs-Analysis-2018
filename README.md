# Logs Analysis Project - Robin Edmunds 2018

## Environment

Development environment is an __Ubuntu 18.04__ host running __Vagrant/libvirt__ with
__debian/jessie64 (v8.11.0)__ box.

### Versions
- psql 9.4.18
- Python 3.4.2
- pip3 18
- psycopg2 2.5.4
- git version 2.1.4

## Usage
Run __main.py__ in your python3 interpreter: -
> $ python3 main.py

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

## License
> MIT License
>
> Copyright (c) 2018 Robin Edmunds
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
