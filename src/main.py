#main.py

#Import sample logs 
from src.parsers import load_logs

logs = load_logs("data/sample_logs.csv")

#print logs 
print(logs.head())
print("Total records:", len(logs))
