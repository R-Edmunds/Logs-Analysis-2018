#!/usr/bin/python3
#
# Logs Analysis project - Robin Edmunds
#
# Dev env Debian/Jessie vagrant/libvirt vm with following software version: -
# - Python 3.4.2
# - pip3 18
# - psycopg2 2.5.4
# - git version 2.1.4

import psycopg2, os

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
    the most popular article at the top.

    Define and submit SQL query. Format and print respone."""

    print("1. What are the most popular three articles of all time? Which "
        + "articles have been accessed the most?\n")

    query = """SELECT COUNT(log.path) AS hits, log.path FROM log
                WHERE log.path LIKE '/article/%'
                AND log.status = '200 OK' AND log.method = 'GET'
                GROUP BY log.path ORDER BY hits DESC LIMIT 3;"""

    response = db_query(query)

    for i, j in enumerate(response):
        """Convert tuple to list to allow writing. Format "path" and add comma
        seperator to "hits". Print output."""
        j = list(j)
        j[1] = j[1].replace("/article/", "").replace("-", " ").title()
        j[0] = str(format(j[0], ',d'))
        print("    Title:  '{1}'  -  {0} views".format(*j))

def query2():
    """2. Who are the most popular article authors of all time? That is, when
    you sum up all of the articles each author has written, which authors get
    the most page views? Present this as a sorted list with the most popular
    author at the top."""

    print("2. Who are the most popular article authors of all time?\n")

    # query = """SELECT COUNT(log.path) AS hits, log.path FROM log
    #             WHERE log.path LIKE '/article/%'
    #             AND log.status = '200 OK' AND log.method = 'GET'
    #             GROUP BY log.path ORDER BY hits DESC LIMIT 3;"""
    #
    # response = db_query(query)
    #
    # for i, j in enumerate(response):
    #     """Convert tuple to list to allow writing. Format "path" and add comma
    #     seperator to "hits". Print output."""
    #     j = list(j)
    #     j[1] = j[1].replace("/article/", "").replace("-", " ").title()
    #     j[0] = str(format(j[0], ',d'))
    #     print("    Title:  '{1}'  -  {0} views".format(*j))


if __name__ == '__main__':
    os.system("clear")      # clear console on unix-like systems
    print("\n-----------------------------------\n"
        + "-  Logs Analysis - Robin Edmunds  -\n"
        + "-----------------------------------\n")
    # query1()
    query2()
    print()
