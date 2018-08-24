#!/usr/bin/python3

# Logs Analysis project - Robin Edmunds
#
# Dev env Debian/Jessie vagrant/libvirt vm with following software version: -
# - Python 3.4.2
# - pip3 18
# - psycopg2 2.5.4
# - git version 2.1.4

# 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
#
# Example:
#
# "Princess Shellfish Marries Prince Handsome" — 1201 views
# "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
# "Political Scandal Ends In Political Scandal" — 553 views

import psycopg2, os

def db_query(query):
    """This function receives SQL statements and executes them"""
    conn = psycopg2.connect("dbname=news")     # connect to db "news" on localhost
    cursor = conn.cursor()      # assign conn.cursor() object to var, "cursor"

    cursor.execute(query)
    response = cursor.fetchall()

    print("Raw output:", response)      # raw output for testing

    conn.close()
    # return reversed(output)

def query1():
    """1. What are the most popular three articles of all time? Which articles
    have been accessed the most? Present this information as a sorted list with
    the most popular article at the top."""

    print("1. What are the most popular three articles of all time? Which articles have been accessed the most?\n")



if __name__ == '__main__':
    os.system("clear")      # clear console on unix-like systems
    print("\n-----------------------------------\n" +
        "-  Logs Analysis - Robin Edmunds  -\n" +
        "-----------------------------------\n")
    query1()
    # test_query = "SELECT * FROM authors LIMIT 10;"
    # db_query(test_query)
