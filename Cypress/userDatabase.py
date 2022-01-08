import sqlite3
from userInfoClass import userInfo

conn = sqlite3.connect('loginInfo.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userInformation (
             firstname text NOT NULL,
             lastname text NOT NULL,
             address text NOT NULL,
             phonenumber text NOT NULL,
             email text NOT NULL,
             username text NOT NULL PRIMARY KEY,
             password text NOT NULL,
             secretQuestion text NOT NULL
             )""")


# def createDatabase():
#     conn = sqlite3.connect('loginInfo.db')
#
#     c = conn.cursor()
#
#     c.execute("""CREATE TABLE userInformation (
#                  firstname text NOT NULL,
#                  lastname text NOT NULL,
#                  address text NOT NULL,
#                  phonenumber text NOT NULL,
#                  email text NOT NULL,
#                  username text NOT NULL PRIMARY KEY,
#                  password text NOT NULL,
#                  secretQuestion text NOT NULL
#                  )""")
#
#     conn.commit()

def createNewUser(newUser):
    
    with conn:
        c.execute("INSERT INTO userInformation VALUES (:firstname, :lastname, :address, :phonenumber, :email, :username, :password, :secretQuestion)", {'firstname': newUser.firstname, 'lastname': newUser.lastname, 'address': newUser.address, 'phonenumber': newUser.phonenumber, 'email': newUser.email, 'username': newUser.username, 'password': newUser.password, 'secretQuestion': newUser.secretQuestion})

def getUserByUsername(username):
    u = c.execute("SELECT * FROM userInformation WHERE username=:username", {'username': username}).fetchall()
    return u

  
def updatefirstname(firstname,username):
    with conn:
        c.execute("""UPDATE userInformation SET firstname = :firstname
                    WHERE username = :username""",
                    {'firstname': firstname, 'username': username})

def updatelastname(lastname,username):
    with conn:
        c.execute("""UPDATE userInformation SET lastname = :lastname
                    WHERE username = :username""",
                    {'lastname': lastname, 'username': username})

def updateaddress(address,username):
    with conn:
        c.execute("""UPDATE userInformation SET address = :address
                    WHERE username = :username""",
                    {'address': address, 'username': username})

def updatephone(phonenumber,username):
    with conn:
        c.execute("""UPDATE userInformation SET phonenumber = :phonenumber
                    WHERE username = :username""",
                    {'phonenumber': phonenumber, 'username': username})

def updateemail(email,username):
    with conn:
        c.execute("""UPDATE userInformation SET email = :email
                    WHERE username = :username""",
                    {'email': email, 'username': username})

def updatepw(password,username):
    with conn:
        c.execute("""UPDATE userInformation SET password = :password
                    WHERE username = :username""",
                    {'password': password, 'username': username})

def updatesecretQ(secretQuestion,username):
    with conn:
        c.execute("""UPDATE userInformation SET secretQuestion = :secretQuestion
                    WHERE username = :username""",
                    {'secretQuestion': secretQuestion, 'username': username})
  

user1 = userInfo('Sam', 'Tom', '1 Dundas St E', '416-979-5000', 'SamTom@cypress.ca', 'SamTom', 'password1', 'Blue')
user2 = userInfo('Michael', 'Tom', '2 Dundas St E', '416-979-5001', 'MichaelTom@cypress.ca', 'MichaelTom', 'password2', 'Green')
user3 = userInfo('James', 'Tom', '3 Dundas St E', '416-979-5002', 'JamesTom@cypress.ca', 'JamesTom', 'password3', 'Yellow')

#createNewUser(user1)
#createNewUser(user2)
#createNewUser(user3)

#print(getUserByUsername('MichaelTom'))
#print(getUserByUsername('SamTom'))
#print(getUserByUsername('JamesTom'))
#print(getUserByUsername(''))

#updateAddress(364, '888 Queen St W')

conn.commit()
# <<<<<<< HEAD
# #conn.close()
# =======
# #conn.close()
# >>>>>>> 0271a0e595b6bb98f263a6eee03c0d485bc96963
