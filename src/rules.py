from src import config

import pandas as pd

def mult_failed_login(logs):
    failure_counts = {}     #initialize dicts to store usernames with their associated number of failed logins

    for x, row in logs.iterrows():
        event = str(row[config.EVENT_COL]).strip().upper()  #gets the event that happened and universalizes its format

        if event == "FAILED":   #checks if event was a failed login, and counts and stores properly
            username = row[config.USERNAME_COL]
            failure_counts[username] = failure_counts.get(username, 0) + 1


    flagged_users = {}      #take only usernames that are flagged in this dict
    for username, count in failure_counts.items():
        if count >= config.MAX_FAILED_LOGINS:
            flagged_users[username] = count

    return flagged_users


def unusual_login_time(logs):
    timestamps = pd.to_datetime(logs[config.TIMESTAMP_COL], errors = "coerce")      #stores date AND time of each logina attempt
    hour_login = timestamps.dt.hour #stores the hour of each login attempt


    ineligible_logins = (
        timestamps.notna()          #gets the timestamps that arent null
        & (hour_login >= config.UNUSUAL_HOUR_START)     #ANDS it with the times that are between unusual hours to flag them to put into different dict
        & (hour_login <= config.UNUSUAL_HOUR_END)

    )

    return logs.loc[ineligible_logins, config.USERNAME_COL].value_counts().to_dict()  #returns a dict of usernames and their number of logins during unusual hours