"""
Subject: CP1404

Testing github.

Student name: Matthew Ballarino
Student number: 1329475
"""
import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)



