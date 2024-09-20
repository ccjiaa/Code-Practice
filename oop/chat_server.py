class User:
    def __init__(self, name, id, username, password):
        self.name = name
        self.id = id
        self.username = username
        self.password = password
        self.true_status = "Online"
        self.visible_status = "Online"

        self.friend_list = []
        self.friend_invites = []
        self.message_box = ""

    def login(self, username, password):
        if self.true_status is "Online":
            return "Already logged in."
        else:
            if username is self.username:
                if password is self.password:
                    self.true_status = "Online"
                    return 1 #indicates successful login
                else:
                    return "Wrong password, please try again."
            else:
                return "Wrong username, please try again."
        
        return "Error, please try again." #failsafe

    def logoff(self):
        if self.true_status is "Offline":
            return #do nothing, already logged off
        else:
            self.true_status = "Offline"

    def set_visible_status(self, cur_status):
        if cur_status is "Do Not Disturb":
            self.visible_status = "Do Not Disturb"
        elif cur_status is "Idle":
            self.visible_status = "Idle"
        elif cur_status is "Online":
            self.visible_status = "Online"
        elif cur_status = "Offline":
            self.visible_status = "Offline"
        else:
            return #do nothing if cur_status is not a valid status


class Message:
    def __init__(self, content, sender):
        self.content = sender + ": " + content


class Chat_Server:
    def __init__(self):
        self.server_members = []
    
    def create_new_account(self, name, id, username, password):
        new_user = User(name, id, username, password)
        self.server_members.append(new_user)

    def send_message(self, message, sender, receiver):
        new_message = Message(message, sender)
        receiver.message_box += "\n" + new_message

    def send_friend_invite(self, sender, receiver):
        receiver.friend_invites.append(sender)
    
    def accept_friend_invite(self, sender, receiver):
        if sender in receiver.friend_invites:
            for i in range (len(receiver.friend_invites)):
                if receiver.friend_invites[i] is sender:
                    receiver.friend_invites.pop(i)
                    break
            receiver.friend_list.append(sender)
            sender.friend_list.append(receiver)
        else:
            return "Friend not found"

    
