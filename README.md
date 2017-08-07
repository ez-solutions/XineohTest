# XineohTest
This repository is made for the interview test for Xineoh.

## Database Description

### Table 1
name: **user_interaction**

Contains user (identified by *userID*) actions (*yes*, *no*, *maybe*, *never*) with certain items (*targetID*)


### Table 2
name: **user_interaction_results**

Contains the correlated *userID*, *interatction* (*yes*, *no*, *maybe*, *never*), and the count of values (*missing_count*) were removed for the purpose of this test. The *results* column will contain the final results provided by the program.

## Requirements
* Python 3.6
* pandas
* pymysql

## Run Program
```
$ python user_interaction.py
```

### NB
Since the *results* column in table *user_interaction_results* was updated during the trial runs, there is no more *NULL* valued results, rerun the program won't have any effects on the results.