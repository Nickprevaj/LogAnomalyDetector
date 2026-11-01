# Log Anomaly Detector

A cybersecurity tool that reads login/network logs from CSV files and flags suspicious activity.

**Team:** Nicholas Prevaj, Landon Anstey, Cullen Chadwick, David Cunha

## Project Goal

Build a tool that ingests login and network logs from CSV files and flags suspicious activity, including:

- Repeated failed logins
- Impossible travel (logins from distant locations in an implausibly short time)
- Unusual ports
- Activity outside normal hours

**Concepts used:** file I/O, dictionaries, functions, conditionals, NumPy / scikit-learn clustering.

## Tooling and Workflow

- **IDE:** VS Code (chosen over Arduino IDE for its extension and environment support)
- **Collaboration:** VS Code Live Share, so we can code together without constantly pushing to Git

## Week 1 - Reflection

Our team spent the week brainstorming how to approach the cybersecurity log anomaly detector. We decided on our main IDE: we chose VS Code over Arduino IDE because it is compatible with extensions and environments. We found that our method of collaboration would be most effective using the LiveShare extension. This makes the coding process easier because we do not have to push to Git constantly. We are still deciding on methods to read network logs from CSV files and flag suspicious activity. We have decided on our workflow and plan to explore ways to implement our detector.

## Planned Structure

```
LogAnomalyDetector/
├── data/            # sample CSV logs
├── src/             # detector modules
├── requirements.txt
└── README.md
```

## Getting Started

```bash
git clone https://github.com/Nickprevaj/LogAnomalyDetector.git
cd LogAnomalyDetector
pip install -r requirements.txt
```
