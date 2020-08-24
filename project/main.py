import sys
import os

from report.reports import trigger

def main():
    print("Triggering COVID-19 mail service..")
    trigger()

main()