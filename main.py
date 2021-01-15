# This is a sample Python script.
import os,re
from flask import Flask
import compress
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "./haha.jpg"



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.    print(ipv4)
if __name__ == '__main__':
    print_hi('ccp')
    print(os.popen("d:").read())
    print(os.popen("dir").read())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
