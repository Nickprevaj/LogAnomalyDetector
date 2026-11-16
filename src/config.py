#Purpose: store projects shared settings and constants 
INPUT_FILE = "data/sample_logs.csv"
OUTPUT_FILE = "output/anomaly_report.csv"

#CSV column names
TIMESTAMP_COL = "Timestamp"
USERNAME_COL = "Username"
IP_COL = "IP Address"
EVENT_COL = "Event"
PORT_COL = "Port"

#Detection thresholds
MAX_FAILED_LOGINS = 5
UNUSUAL_HOUR_START = 0
UNUSUAL_HOUR_END = 5

#Machine learning settings
CONTAMINATION = 0.05 #estimated 5% of logs are anomolies 
RANDOM_STATE = 42 #controls randomization 
