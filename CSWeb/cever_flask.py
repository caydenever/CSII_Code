'''
Author: Cayden Ever
Sources: Mr. Campbell, Titanic.Csv, W3schools for read/write
Description: creates a form using flask that writes to a csv file
Date: 5/26/2026
Bugs: n/a
'''
from flask import Flask, request, render_template
import csv
import sys
import os # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    #print(app.url_map)
    #print('line 17')            # Print statements go to your console
    
    #return render_template("index.html")
    return "Hello, World!"  # Return this string as a response to the client


@app.route("/export_csv") #set the url root of export_csv
def export_csv():
    '''
    Takes in form data from form.html and writes it out to sleep_data.csv
    args:
        none
    returns: success message when all data is written out
    '''
    #get all form data and set to local variable using request.args.get
    try:
        fname = request.args.get('fname')
        lname = request.args.get('lname')
        grade = request.args.get('grade')
        bedtime = request.args.get('bedtime')
        wakeup = request.args.get('wakeup')
        weekend_shift = request.args.get('weekend_shift')
        sleep_quality = request.args.get('sleep_quality')
        gpa = request.args.get('gpa')
        honors = request.args.get('honors')
        tired = request.args.get('tired')
        sports = request.args.get('sports')
        clubs = request.args.get('clubs')
        screen_time = request.args.get('screen_time')
        caffiene = request.args.get('caffiene')
        mood = request.args.get('mood')
    except ValueError:
        print("error pulling form data to local variables.") #print error message if there is a value error
    with open('sleep_data.csv', 'w', newline='') as csvfile: #open up the csv file sleep_data to write to it
        csvfile.write("First Name,Last Name,Grade,Bedtime,Wakeup,Weekend Shift,Sleep Quality,GPA,Honors,Tired,Sports,Clubs,Screen Time,Caffeine,Mood\n")#write out the titles of each string of data
        #convert the data received from the form into strings and add commas between each
        data = str(fname) + ","  + str(lname) + ","  + str(grade) + ","  + str(bedtime) + ","  + str(wakeup) + ","  + str(weekend_shift) + ","  + str(sleep_quality) + ","  + str(gpa) + ","  + str(honors) + ","  + str(tired) + ","  + str(sports) + ","  + str(clubs) + ","  + str(screen_time) + ","  + str(caffiene) + "," + str(mood)
        #write out the data
        csvfile.write(data) 
    return "Data saved successfully!" #return success message


@app.route("/display_form")#set the page of display_form to render form.html
def display_form():
    return render_template("form.html") #display the form.html page


    

if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp