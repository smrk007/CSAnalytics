:: This file updates the data in the CSAnalytics project
:: once daily at 7:00 AM, executed by the windows task
:: scheduler application.

@echo off
python csanalytics.py 2>> bat_debug.log
EXIT

