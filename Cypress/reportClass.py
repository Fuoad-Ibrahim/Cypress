class Report:
    def __init__(self, username, address, issue):
        self.number = None
        self.username = username
        self.address = address
        self.issue = issue

    def __repr__(self):
        return "Report({}, '{}', '{}', '{}')".format(self.number, self.username, self.address, self.issue)

