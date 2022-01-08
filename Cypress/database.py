import sqlite3
from userInfoClass import userInfo


class database(object):

    loggedUsers = []
    currentUser = ''
    currentUserInfo = None

    @staticmethod
    def register(firstname, lastname, address, phonenumber, email, username, password, secretQuestion):
        try:
            conn = sqlite3.connect("loginInfo.db")
            cursor = conn.cursor()
            query = 'INSERT INTO userInformation VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
            cursor.execute(query, (firstname, lastname, address, phonenumber, email, username, password, secretQuestion))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect("loginInfo.db")
        cursor = conn.cursor()
        query = 'SELECT * FROM userInformation WHERE username = ? AND password = ?'
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        #print(result[0])
        if (len(result) > 0):
            database.currentUserInfo = userInfo(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], '', '')
            #print(database.currentUser)
            conn.close()
            database.loggedUsers.append(username)
            database.currentUser = username
            return True
        conn.close()
        return False

    @staticmethod
    def logout():
        database.loggedUsers.remove(database.currentUser)
        database.currentUser = ''
        database.currentUserInfo = None

    @staticmethod
    def isLoggedIn(username):
        if (username in database.loggedUsers):
            return True
        return False

    @staticmethod
    def getCurrentUser():
        return database.currentUser

    @staticmethod
    def retrievePassword(username, secretQuestion):
        conn = sqlite3.connect("loginInfo.db")
        cursor = conn.cursor()
        query = 'SELECT password FROM userInformation WHERE username = ? AND secretQuestion = ?'
        cursor.execute(query, (username, secretQuestion))
        result = cursor.fetchone()
        if result == None:
            conn.close()
            return "Not Found"
        else:
            pwd = result[0]
            conn.close()
            return pwd
        
        
    @staticmethod
    def retrievesecretQAnswer(username):
        conn = sqlite3.connect("loginInfo.db")
        cursor = conn.cursor()
        query = 'SELECT secretQuestion FROM userInformation WHERE username = ?'
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        secretQ = result[0]
        return secretQ

    @staticmethod
    def delete(username):
        database.loggedUsers.remove(username)
        conn = sqlite3.connect("loginInfo.db")
        cursor = conn.cursor()
        query = 'DELETE FROM userInformation WHERE username=?'
        cursor.execute(query, (username,))
        conn.commit()
        conn.close()
        return True


if __name__ == "__main__":
    print(database.login('MichaelTom', 'password2'))
