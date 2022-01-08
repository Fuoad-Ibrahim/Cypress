import sqlite3
import random
from reportClass import Report

conn = sqlite3.connect('reports.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS reports (
            number integer,
            username text,
            address text,
            issue text
            )""")


def createNewReport(report):
    number = generateNumber(random.randint(1, 4000))
    report.number = number

    with conn:
        c.execute("INSERT INTO reports VALUES (:number, :username, :address, :issue)", {'number': number, 'username': report.username, 'address': report.address, 'issue': report.issue})

def generateNumber(generatednumber):
    c.execute("SELECT * FROM reports WHERE number = :number", {'number': generatednumber})
    if c.fetchone() != None:
        return generateNumber(random.randint(1,4000))
    else:
        return generatednumber

def getReportsByUsername(username):
    return c.execute("SELECT * FROM reports WHERE username=:username", {'username': username}).fetchall()

def updateAddress(number, address):
    with conn:
        c.execute("""UPDATE reports SET address = :address
                    WHERE number = :number""",
                  {'number': number, 'address': address})

def updateIssue(number, issue):
    with conn:
        c.execute("""UPDATE reports SET issue = :issue
                    WHERE number = :number""",
                    {'number': number, 'issue': issue})

def deleteReport(number):
    with conn:
        c.execute("DELETE from reports WHERE number = :number",
                  {'number': number})

        
def deleteByUser(username):
    with conn:
        c.execute("DELETE from reports WHERE username = :username",
                  {'username': username})

#report1 = Report('admin', '1 Dundas St E', 'Potholes')
#report2 = Report('toronto', '100 Queen St W', 'City Property Vandalism')
#report3 = Report('admin', '350 Victoria St', 'Mold and Spore Growth')

# createNewReport(report1)
# createNewReport(report2)
# createNewReport(report3)

# print(getReportsByUsername('bill'))

#updateAddress(364, '888 Queen St W')

#print(getReportsByUsername('toronto'))

#print(getReportsByUsername('SamTom').fetchone())

conn.commit()
#conn.close()
