#########################################
# Author - Shivam Kapoor (mailme@shivamkapoor.me)
#
# A small python script written for personal convineance to calculate
# CGPA by scraping academic history webpage.
#
# Github : https://github.com/ConanKapoor/VIT-CGPA-Scrapy-Calculator
#########################################

# Importing Essesnsials.
from bs4 import BeautifulSoup
from pyfiglet import Figlet
import urllib.request
import xlsxwriter
import time
import sys
import os

# Making a log file.
logs = open('logs.txt','w')
logs.write("The following errors were encountered during scraping ->\n\n")

# Creating Output folder.
if (os.path.exists("Academic_Transcript")):
    delete = str('rm -r Academic_Transcript')
    os.system(delete)
    os.makedirs("Academic_Transcript")
else:
    os.makedirs("Academic_Transcript")

# Printing unecessary information for 'wanna be cool' people.
# Comment all for minimal script.
os.system('cls' if os.name == 'nt' else 'clear')
banner = Figlet(font='slant')
print("\n")
print (banner.renderText('CGPA CALC'))
print ("\t  >>>>>>> VIT CGPA Calculator <<<<<<<")
print ("\t  >>>>>>  Author : ConanKapoor <<<<<<")
print ("\t  >>>>>> API by : sridharswain <<<<<<\n")

# Printing unecessary information for 'wanna be cool' people #2
print (">>> Now I have to do image processing shit to fill  <<<\n>>> captcha so your sorry ass don't have to log in. <<<\n>>>\t\t\t\t    - Sridhar Swain <<<")

# Printing unecessary information for 'wanna be cool' people #3
print ("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

try:
    Verbose = input(">>> Do you want verbose output? (Y or N) : ")
    Username = input(">>> Please feed your Registration No     : ")
    Password = input(">>> Please feed your Password            : ")
    url ="https://vitgrades.herokuapp.com/grades?userName=" + Username + "&password=" + Password

    # Printing unecessary information for 'wanna be cool' people #4
    print ("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

    # Printing unecessary information for 'wanna be cool' people #5
    print(">>> Request sent to server.")
    time.sleep(1)
    print(">>> Done!!!\n")
    print(">>> Cracking Captcha.")
    time.sleep(1)
    print(">>> Done!!!\n")
    print(">>> Receiving data from server. This will take time.")

    # Collecting html content.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    # Using BeautifulSoup to parse Students data.
    soup = BeautifulSoup(response.read(),"lxml")
    infoTable = soup.find("table",{"height": "58"})
    infoStudent = infoTable.find_all("td",{"bgcolor":"#EDEADE"})

    # Scraping Student data
    Regno = infoStudent[0].text
    Name = infoStudent[1].text
    Branch = (infoStudent[2].text).replace('B.Tech. ','')
    School = infoStudent[3].text

    # Using BeautifulSoup to parse Grades data.
    gradesTable = soup.find("table",{"id":"hist"})
    infoGrades = gradesTable.find_all("tr",{"bgcolor":"#EDEADE"})

    # Initiating XLSX file
    filepath = 'Academic_Transcript/Grades-'+ Regno +'.xlsx'
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'S.No.', bold)
    worksheet.write('B1', 'Course Code', bold)
    worksheet.write('C1', 'Course Title', bold)
    worksheet.write('D1', 'Course Type', bold)
    worksheet.write('E1', 'Credits', bold)
    worksheet.write('F1', 'Grade', bold)
    worksheet.write('G1', 'Exam Held', bold)
    worksheet.write('H1', 'Result Date', bold)

    rows = 1
    for subject in range(len(infoGrades)):
        gradeRow = infoGrades[subject]
        gradeData = gradeRow.find_all("td")

        # Putting data in Worksheet.
        if(gradeData[5].text != '-'):
            worksheet.write(rows, 0, rows)
            for i in range(1,8):
                worksheet.write(rows, i, gradeData[i])
        else:
            continue;

# except Exception:
#     print("    >!>!> Exceptioncaught - skipping to next grade.")
#     print("          Most Probably Network error.")
#     print("          GPA will suffer\n")
#     logs.write(" Outer Exception error.\n\n")
#     pass
#
# except KeyboardInterrupt:
#     print("\n\n>>> Interrupt received! Exiting cleanly...")
#     logs.write("End of logs - Abruptly Ended")
#     logs.close()
#     sys.exit()

logs.close()
############################### END OF SCRIPT :) ##############################
