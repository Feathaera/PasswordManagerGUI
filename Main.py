import tkinter
import customtkinter
import hashlib



accountusername = ""
accountpassword = ""
databaseuser = ""


#------------------------------------------
#           Functions
#------------------------------------------
def login():
    nologinaccountfoundLabel.pack_forget()
    currentline = 0
    username = loginusernameentry.get()
    password = loginpasswordentry.get()
    password = password + "\n"
    global databaseuser
    databaseuser = loginusernameentry.get()
    file = open("users.txt", "r")
    for line in file:
        currentline = currentline + 1
        if username in line: # Checks to see if the username can be found in the registered users file
            line = file.readlines(currentline -1)
            if password in line:
                file.close()
                print("You have successfully logged in! Welcome user")
                mainmenui()
            else:
                print("Your password could not be recognised, please try again")
        else:
            pass
    nologinaccountfoundLabel.pack()
    file.close()


def register():
    username = registerusernameentry.get()
    password = registerpasswordentry.get()
    password = password+"\n"
    found = False
    file = open("users.txt", "r")
    for line in file:
        if username in line:
            print("This user already exists! Please try logging in instead")
            found = True
            loginui()
    
    if not found:
        print("Sucessfully registered user!")
        file = open("users.txt", "a")
        file.write(username+"\n"+password)
        file.close()
        filecreation(username)
        loginui()



def filecreation(username):
    file = open(username+".txt", "w") # generates a file for the user if newly created (Might be best moved to register)
    file.close()
    return

def checkaccount(service, username, databaseuser):
    currentline = 2
    file = open(databaseuser+".txt", "r") # Opens up the file for just that user
    lines = file.readlines()
    file.close()
    for line in lines:
        if line == service: # If the service/website is already registered
            lineusername = lines[currentline-1].strip() # Gets the current position of the where the file is reading
            username = username.strip()
            if lineusername==username: # If the username has already been registered for the account
                print("You have already registered this account!") 
                mainmenui()
                return False
            else:
                print("They do not match!")
                currentline = currentline+3 #Moves the current location of the list along by 3 spaces (Aka where the next username is)
    print("Account not detected! Updating database now....")
    return True


def CreateLogin():
    global databaseuser
    databaseuser = loginusernameentry.get()
    service = newloginservicenameEntry.get()
    service = service+"\n"
    username = newloginusernameEntry.get()
    username = username+"\n"
    password = newloginpasswordEntry.get()
    if checkaccount(service, username, databaseuser) == True:
        file = open(databaseuser+".txt", "a")
        print("Fie opened")
        file.write(service + username + password + "\n")
        print("Written to file")
        newlogincreatedLabel.pack()
        print("Packaged the new ui")
        mainmenui()


def ViewLogin():
    NoaccountFoundLabel.pack_forget()
    global databaseuser
    global accountusername
    global accountpassword
    found = False
    currentline = 0
    file = open(databaseuser+".txt", "r")
    lines = file.readlines()
    service = viewaccountEntry.get()
    for line in lines:
        currentline = currentline+1
        if service in line:
            accountusername = lines[currentline]
            viewaccountusernameLabel.configure(text=f"Your username is: {accountusername}")
            viewaccountusernameLabel.pack()
            accountpassword = lines[currentline+1]
            viewaccountpasswordLabel.configure(text=f"Your password is: {accountpassword}")
            viewaccountpasswordLabel.pack()
            found = True
    if not found:
        file.close()
        viewaccountusernameLabel.pack_forget()
        viewaccountpasswordLabel.pack_forget()
        NoaccountFoundLabel.pack()





#----------------------------------------------------------------
#                   UI Definitions
#--------------------------------------------------------------

def registerui():
    LoginFrame.pack_forget()
    RegisterFrame.pack()

def loginui():
    RegisterFrame.pack_forget()
    MainMenuFrame.pack_forget()
    LoginFrame.pack()

def mainmenui():
    ViewloginUIFrame.pack_forget()
    LoginFrame.pack_forget()
    app.after(2500, createloginuiFrame.pack_forget())
    MainMenuFrame.pack()
    
def createloginui():
    MainMenuFrame.pack_forget()
    createloginuiFrame.pack()

def viewloginui():
    MainMenuFrame.pack_forget()
    ViewloginUIFrame.pack()
 
#Theme settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Setting up the main window
app = customtkinter.CTk()
app.geometry("720x480") # Size of the window
app.title("Daybreaks Password manager") # Title of the window




# Login window frame (Default frame)
LoginFrame = customtkinter.CTkFrame(app)
LoginFrame.pack()
RegisterFrame = customtkinter.CTkFrame(app)
MainMenuFrame = customtkinter.CTkFrame(app)
createloginuiFrame = customtkinter.CTkFrame(app)
ViewloginUIFrame = customtkinter.CTkFrame(app)
#----------------------------------------------------------------
#               UI ELEMENTS
#----------------------------------------------------------------
#                   Login
#----------------------------------------------------------------

# Programme name title
programmetitlelabel = customtkinter.CTkLabel(LoginFrame, text="Password manager", font=("Arial", 25))
programmetitlelabel.pack(pady=10)

# username
loginusernamelabel = customtkinter.CTkLabel(LoginFrame, text="Please enter your username") #App is the location where we wanna put it/the frame
loginusernamelabel.pack() #Adds the UI

loginusernameentry = customtkinter.CTkEntry(LoginFrame, width=350, height=40)
loginusernameentry.pack()

# Password
loginpasswordlabel = customtkinter.CTkLabel(LoginFrame, text="Please enter your password")
loginpasswordlabel.pack()

loginpasswordentry = customtkinter.CTkEntry(LoginFrame, width=350, height=40, show="*")
loginpasswordentry.pack()

# Login button
loginbutton = customtkinter.CTkButton(LoginFrame, text="Login", command=login) # Command allows you to pass in functions to buttons
loginbutton.pack(pady=10)

nologinaccountfoundLabel = customtkinter.CTkLabel(LoginFrame, text="Your account could not be found", text_color="red")

# Register button
registerbutton = customtkinter.CTkButton(LoginFrame, text="Register", command=registerui)
registerbutton.pack(pady=10)
#-----------------------------------------------------------------------------
#                   Register
#-----------------------------------------------------------------------------
registeraccountlabel = customtkinter.CTkLabel(RegisterFrame, text="Register an account", font=("Arial", 25))
registeraccountlabel.pack()

registerusernamelabel = customtkinter.CTkLabel(RegisterFrame, text="Please enter your username")
registerusernamelabel.pack()

registerusernameentry = customtkinter.CTkEntry(RegisterFrame, width=350, height=40)
registerusernameentry.pack()

registerpasswordlabel = customtkinter.CTkLabel(RegisterFrame, text="Please enter your password")
registerpasswordlabel.pack()

registerpasswordentry = customtkinter.CTkEntry(RegisterFrame, width=350, height=40)
registerpasswordentry.pack()


CreateAccountButon = customtkinter.CTkButton(RegisterFrame, text="Register account", command=register)
CreateAccountButon.pack(pady=10)

LoginReturnButton = customtkinter.CTkButton(RegisterFrame,text="Login", command=loginui)
LoginReturnButton.pack()

#--------------------------------------------------------------------------------
#           Main menu
#--------------------------------------------------------------------------------

MainMenuLabel = customtkinter.CTkLabel(MainMenuFrame, text="Please select an action", font=("Arial", 25))
MainMenuLabel.pack()

CreateloginButton = customtkinter.CTkButton(MainMenuFrame, text="Create new login", command=createloginui) 
CreateloginButton.pack(pady=50)

ViewloginButton = customtkinter.CTkButton(MainMenuFrame, text="View a login", command=viewloginui)
ViewloginButton.pack()

SignOffButton = customtkinter.CTkButton(MainMenuFrame, text="Sign out", command=loginui)
SignOffButton.pack(padx=100, pady=100)



#-----------------------------------------------------------------------------
#               Create new login UI
# ----------------------------------------------------------------------------
newloginTitle = customtkinter.CTkLabel(createloginuiFrame, text="Register a new service", font=("Arial", 25))
newloginTitle.pack(pady=10)

newloginservicenameLabel = customtkinter.CTkLabel(createloginuiFrame, text="Enter the name of the service here")
newloginservicenameLabel.pack(pady=10)

newloginservicenameEntry = customtkinter.CTkEntry(createloginuiFrame,width=350, height=40)
newloginservicenameEntry.pack()

newloginusernameLabel = customtkinter.CTkLabel(createloginuiFrame, text="Enter your username for the site")
newloginusernameLabel.pack(pady=10)

newloginusernameEntry = customtkinter.CTkEntry(createloginuiFrame, width=350, height=40)
newloginusernameEntry.pack()

newloginpasswordLabel = customtkinter.CTkLabel(createloginuiFrame, text="Please enter your password for the site")
newloginpasswordLabel.pack(pady=10)

newloginpasswordEntry = customtkinter.CTkEntry(createloginuiFrame, width=350, height=40)
newloginpasswordEntry.pack()

newloginconfirmButton = customtkinter.CTkButton(createloginuiFrame, text="Confirm", command=CreateLogin)
newloginconfirmButton.pack(pady=25)

newlogincreatedLabel = customtkinter.CTkLabel(createloginuiFrame, text="Account registered", text_color="green")

#------------------------------------------------------------------------------
#                   View login
#------------------------------------------------------------------------------

viewaccountabel = customtkinter.CTkLabel(ViewloginUIFrame, text="Please enter the name of the service")
viewaccountabel.pack()

viewaccountEntry = customtkinter.CTkEntry(ViewloginUIFrame, width=350, height=40 )
viewaccountEntry.pack()

viewaccountButton = customtkinter.CTkButton(ViewloginUIFrame, text="Search for account", command=ViewLogin)
viewaccountButton.pack()


NoaccountFoundLabel = customtkinter.CTkLabel(ViewloginUIFrame, text="No account found")

viewaccountusernameLabel = customtkinter.CTkLabel(ViewloginUIFrame, text=f"Account username: {accountusername}") 
viewaccountpasswordLabel = customtkinter.CTkLabel(ViewloginUIFrame, text=f"Account Password: {accountpassword}") 

viewaccountbackButton = customtkinter.CTkButton(ViewloginUIFrame, text="Go back", command=mainmenui)
viewaccountbackButton.pack(pady=50)





# Run the programme
app.mainloop()