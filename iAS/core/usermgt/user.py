class User:
    def __init__(self, userId="",
                 userName="",
                 gender="",
                 email="",
                 profilePicture=""
                 ):
        self.profilePicture = profilePicture
        self.email = email
        self.gender = gender
        self.userName = userName
        self.userId = userId
