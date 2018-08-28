#!/usr/bin/python3
#
# Logs Analysis project - Robin Edmunds 2018

import datetime
import os
import psycopg2


def db_query(query):
    """This function receives SQL statements and executes them on live DB."""
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(query)
    response = cursor.fetchall()
    conn.close()
    return response


def query1():
    """1. What are the most popular three articles of all time? Which articles
    have been accessed the most? Present this information as a sorted list with
    the most popular article at the top."""

    print("1. What are the most popular three articles of all time? Which " +
          "articles have been accessed the most?\n")

    query = """
        SELECT articles.title, subq.hits FROM articles
        LEFT JOIN
            (SELECT COUNT(log.path) AS hits, log.path FROM log
            WHERE log.path LIKE '/article/%'
            AND log.status = '200 OK' AND log.method = 'GET'
            GROUP BY log.path) AS subq
        ON subq.path LIKE '/article/'||articles.slug
        ORDER BY subq.hits DESC LIMIT 3;
        """

    response = db_query(query)

    for i, j in enumerate(response):
        # Convert tuple to list to allow writing. Format "hits" with comma
        # seperator. Print output.
        j = list(j)
        j[1] = str(format(j[1], ',d'))
        print("    Title:  '{}'  -  {} views".format(*j))


def query2():
    """2. Who are the most popular article authors of all time? That is, when
    you sum up all of the articles each author has written, which authors get
    the most page views? Present this as a sorted list with the most popular
    author at the top."""

    print("2. Who are the most popular article authors of all time?\n")

    query = """
        SELECT authors.name, subq_author.hits FROM authors
        LEFT JOIN
            (SELECT articles.author, CAST(SUM(subq_article.hits) AS INTEGER)
            AS hits FROM articles
            LEFT JOIN
                (SELECT COUNT(log.path) AS hits, log.path FROM log
                WHERE log.path LIKE '/article/%'
                AND log.status = '200 OK' AND log.method = 'GET'
                GROUP BY log.path) AS subq_article
            ON subq_article.path LIKE '/article/'||articles.slug
            GROUP BY articles.author) AS subq_author
        ON authors.id = subq_author.author
        ORDER BY subq_author.hits DESC;
        """

    response = db_query(query)

    for i, j in enumerate(response):
        # Convert tuple to list to allow writing. Format "hits" with comma
        # seperator. Print output.
        j = list(j)
        j[1] = str(format(j[1], ',d'))
        print("    Author:  '{}'  -  {} views".format(*j))


def query3():
    """3. On which days did more than 1% of requests lead to errors? The log
    table includes a column status that indicates the HTTP status code that the
    news site sent to the user's browser. (Refer to this lesson for more
    information about the idea of HTTP status codes.)

    This query makes use of SQL VIEWS, documented in README.md"""

    print("3. On which days did more than 1% of requests lead to errors?\n")

    query = """
        SELECT view_daily_requests.date,
            CAST(view_daily_errors.daily_errors AS REAL) /
            CAST(view_daily_requests.daily_requests AS REAL) AS pc
        FROM view_daily_requests
            JOIN view_daily_errors
            ON view_daily_requests.date = view_daily_errors.date
        WHERE CAST(view_daily_errors.daily_errors AS REAL) /
        CAST(view_daily_requests.daily_requests AS REAL) >= 0.01
        ORDER BY pc DESC;
        """

    response = db_query(query)

    for i, j in enumerate(response):
        # Convert tuple to list to allow writing. Format "pc" as percentage,
        # format date '31 December 2018'. Print output.
        j = list(j)
        j[0] = j[0].strftime("%d %B %Y")
        j[1] = str(format(j[1], '%'))
        print("    Date:  {}  -  {} errors".format(*j))


if __name__ == '__main__':
    os.system("clear")  # clear console on unix-like systems
    print("\n-----------------------------------\n" +
          "-  Logs Analysis - Robin Edmunds  -\n" +
          "-----------------------------------\n")
    query1()
    print("\n\n")
    query2()
    print("\n\n")
    query3()
    print("\n\n")
