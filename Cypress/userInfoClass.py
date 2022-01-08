class userInfo:
    def __init__(self, firstname, lastname, address, phonenumber, email, username, password, secretQuestion):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.username = username
        self.password = password
        self.secretQuestion = secretQuestion

    def __repr__(self):
        return "user('{}', '{}', '{}', '{}', '{}', '{}')".format(self.firstname, self.lastname, self.address, self.phonenumber, self.email, self.username)
