class Userauths():
    def __init__(self):
        self.state=False
        self.User=None

    def StateLog(self , request):
        if request.user.is_authenticated:

            self.User=request.user
            self.state=True
            dic={"State":self.state , "User":self.User}
            return dic
        else:
            self.User = None
            self.state = False
            dic = {"State": self.state, "User": self.User}
            return dic
