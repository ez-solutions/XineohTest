#!user/bin/python
import pymysql
import sys
import pandas as pd
import logging

HOSTNAME = "173.45.91.18"
USERNAME = "test_user_03"
PASSWORD = "qA0OjU4udz4i"
DATABASE = "user_interaction_03"

def get_results(table_name, userid, interaction, missing_count, conn):
    """
    Get user interaction results from a give connection
    Workout user results in a list and return as comma separated string
    """
    get_interaction_query = "SELECT targetID FROM {} \
        WHERE userID={} AND interaction='{}';".format(table_name, userid, interaction)
    print("QUERY: %s" % get_interaction_query)
    user_interactions = pd.read_sql(get_interaction_query, con=conn)
    results = [
        str(i) for i in user_interactions["targetID"][:missing_count * 2]
    ]
    results_str = ",".join(results)
    return results_str

def update_results(table_name, results, userid, interaction, db_cursor, conn):
    """
    Update user interaction results to a given db cursor
    """
    update_result_query = "UPDATE %s \
        SET results='%s' WHERE userID='%s' AND interaction='%s'" % (table_name, results, userid, interaction)
    print("QUERY: %s" % update_result_query)
    db_cursor.execute(update_result_query)
    conn.commit()

def update_user_interaction_results(conn):
    """
    Update user interaction results to user_interaction table
    """
    get_results_query = "SELECT userID, interaction, missing_count, results \
        FROM user_interaction_results WHERE results is NULL;"
    print("QUERY: %s" % get_results_query)
    db_cursor = conn.cursor()
    for results in pd.read_sql(get_results_query, con=conn, chunksize=10):
        for index, row in results.iterrows():
            userid = row["userID"]
            interaction = row["interaction"]
            missing_count = row["missing_count"]
            results = get_results(
                "user_interaction", userid, interaction, missing_count, conn
            )
            print("userID: %s" % userid)
            print("interaction: %s" % interaction)
            print("missing_count: %s" % missing_count)
            print("Updating results: %s " % results)
            update_results("user_interaction_results", results, userid, interaction, db_cursor, conn)

def main():
    """
    """
    db_connection = pymysql.connect(
        host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)

    update_user_interaction_results(db_connection)

    db_connection.close()

if __name__ == '__main__':
    main()
