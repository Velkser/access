class Profile:
    def __init__(self, id):
        self.userid = id
        self.filename = f"profile{id}.txt"




class Site:
    def __init__(self):
        self.__acc = {}
        self.acc_id = {}
        self.fake_acc = {"Unknown": "******"}
        self.__admin_log = False
        
    def registration(self, email, password):
        if email not in self.__acc:
            self.__acc[email] = password
            self.acc_id[email] = len(self.__acc)
            
        
        
    def check_access(self, email, password):
        if email in self.__acc and self.__acc[email] == password:
            return True
        else:
            return False
        
    def set_admin(self, login, password):
        if login == "root" and password == "toor":
            self.__admin_log = True
        else: self.__admin_log = False
        
    def admin_logout(self):
        self.__admin_log = False
        
    def get_acc(self):
        if self.__admin_log:
            return self.__acc
        else: return self.fake_acc
    
    def get_acc_id(self):
        return self.acc_id
    
class User:
    def __init__(self):
        self.name = "Unknown"
        self.__email = "Unknown"
        self.__password = "Unknown"
        self.site = "Unknown"
        self.login = False
        
    def go_to(self, site):
        self.site = site
        
    def signup(self, name, email, password):
        self.name = name
        self.__email = email
        self.__password = password
        self.site.registration(self.__email, self.__password)
        self.profile = Profile(self.site.get_acc_id()[self.__email])
        file = open(self.profile.filename, "w+")
        file.write(f"Name: {self.name}\nEmail: {self.__email}\nStatus: \nPosts: \nImages: \n")
        file.close()
        
    def signin(self, email, password):
        self.__email = email
        self.__password = password
        self.login = self.site.check_access(self.__email, self.__password)
        self.profile = Profile(self.site.get_acc_id()[self.__email])
    

    def set_content(self, txt, index):
        with open(self.profile.filename) as f:
            contents = f.readlines()
        #contents = self.get_content()
        with open(self.profile.filename, 'w') as f:
            for s in range(len(contents)):
                if s == index:
                    #f.write(f"Status: {txt}\n")
                    f.write(contents[s][:-1] + f"{txt}\n")
                else:
                    f.write(contents[s])
            f.close()
            
            
    def set_status(self, txt):
        self.set_content(txt, 2)
            
    def set_post(self, txt):
        self.set_content(txt, 3)
            
    
        
        
github = Site()
python_org = Site()
user1 = User()
user1.go_to(github)
user1.signup("Qwerty", "qwerty@gmail.com", "qwerty123")
user1.signin("qwerty@gmail.com", "qwerty123")

user2 = User()
user2.go_to(github)
user2.signup("Qwerty", "qwerty1@gmail.com", "1qwerty123")
user2.signin("qwerty1@gmail.com", "1qwerty123")

user3 = User()
user3.go_to(github)
user3.signup("Qwerty", "qwerty2@gmail.com", "2qwerty123")
user3.signin("qwerty2@gmail.com", "2qwerty123")

user4 = User()
user4.go_to(python_org)
user4.signup("zstrgfxd", "zfxjyxrs@gmail.com", "zdhsgdhrd")
user4.set_post("My first post")
# github.set_admin("root", "toor")
# users = github.get_acc()


# for user in users:
#     print(f"User mail: {user}\nuser pass: {users[user]}\n")
    
# github.admin_logout()

# users_id = github.get_acc_id()

# for user in users_id:
#     print(f"User mail: {user}\nuser id: {users_id[user]}\n")
user1.set_status("Text3")   
user2.set_status("Delaju huiniu, ogromnuju")
user3.set_status("Test")

