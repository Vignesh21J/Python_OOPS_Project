from Registering import User


class UserData:

    __Users = []

    @classmethod
    def AddUser(cls, Userobj):

        if isinstance(Userobj, User):
            cls.__Users.append(Userobj)
            print("You have been Successfully Registered...")
        else:
            print("Invalid User")

    @classmethod
    def ValidateLogin(cls, Mail, Pass):

        for user in cls.__Users:
            if user.Mailid == Mail and user.Password == Pass:
                return user
        return None
