#!user/bin/python
import pymysql
import sys
import pandas as pd

HOSTNAME = "173.45.91.18"
USERNAME = "test_user_03"
PASSWORD = "qA0OjU4udz4i"
DATABASE = "user_interaction_03"

query_interaction_results = "SELECT userID, interaction, missing_count, interaction, results FROM user_interaction_results LIMIT 10";
print(query_interaction_results)
db_connection = pymysql.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)
for interaction_results in pd.read_sql(query_interaction_results, con=db_connection, chunksize=10):
    for index, row in interaction_results.iterrows():
        row = row.drop_duplicates()
        userid = row["userID"]
        interactioin = row["interaction"]
        missing_count = row["missing_count"]
        query_target_id = "SELECT targetID FROM user_interaction WHERE userID={} AND interaction='{}'".format(userid, interactioin)
        print(query_target_id)
        user_interactions = pd.read_sql(query_target_id, con=db_connection)
        user_interactions = user_interactions[:missing_count * 2]
        results = [str(i) for i in df["targetID"][:missing_count * 2]]
        results_str = ",".join(results)
        print("results: {}".format(results)
        print("result count: {}".format(len(resuts)))
db_connection.close()
