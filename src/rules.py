from src import config

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
