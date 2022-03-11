
# Importing Libraries 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from tkinter import simpledialog
from tkinter.ttk import Progressbar 
import random
import time

ans = 0
chealth = 100
uhealth = 100
uans = 0
tries = 0
winner = "no one... finish the game first to see your results"

# Process: function that creates a question 
def getquestion():
    
    global chealth
    global uhealth
    global tries
    global ans

    # New strategy I researched to place widgets easily 
    subq.place(x = 760, y = 465, width = 100, height = 65)
    
    # Ensures the user can not refresh the answer 
    if tries < 1:
        num1 = random.randint(2, 16)
        num2 = random.randint(2, 16)
        sign = random.choice(signs)
        
        question = str(num1) + sign + str(num2)
        mathq.configure(text = question, fg = "black")
    
        tries+=1
        
        #method to evaluate math questions with python 
        ans = eval(question)

        
    else:
        messagebox.showinfo("Error", "You can not refresh the question, try answerin this question!")
   
# checking answer

def check():
    global chealth
    global uhealth
    global tries
    global ans
    global uans
    global winner
  
    # resets the number of refreshes of a question 
    tries = 0
    
    # checks if a numeric answer has been inputted
    # (a nonnumeric answer is still incorrect) 
    try: 
        uans = int(userinput.get())
    except:
        messagebox.showinfo("Error", "Please enter a numeric value")

        
    subq.place_forget()
    
    # changes damage values, and variable values depending on whether answe is correct of not
    if int(uans) == int(ans):
        udamage = random.choice(damage)
        messagebox.showinfo("Results", "Good Job! You got it correct and have done " + str(udamage)
                            + " damage to your oponent. Click to get your next question")
        chealth = chealth - udamage
        compbar["value"] = chealth
        comphealth.configure(text = chealth)
        
    else:
         messagebox.showinfo("Results", "Better luck next time! The correct answer was "
                             + str(ans) + ". Click to get your next question.")
    
    # Extra information I found online to make the user experience better:
    # the computers damages will be delayed a little
    
    time.sleep(0.5)
    cdamage = random.choice(damage)
    uhealth = uhealth - cdamage
    userbar["value"] = uhealth
    userhealth.configure(text = uhealth)
        
    messagebox.showinfo("Opponent Attacked", "Oh no! Your opponent has attacked and done "
                        + str(cdamage) + " damage to you")
        
    # Checks if there is a winner
    if chealth < 1 and chealth < uhealth and not uhealth< 1:
        # Sets progress bars
        userbar["value"] = uhealth
        compbar["value"] = chealth
        
        winner = "YOU" 
        time.sleep(0.5)
        res = messagebox.askyesno("Results", "Congrats you have beaten your opponent! Want to play again?")
                
        if res == True:
            messagebox.showinfo("Results", "Head over to the first tab and choose a new character to play with!"\
                                "Don't forget to save your data of this battle by clicking on the SAVE button as well!")

                
        else:
            messagebox.showinfo("Results", "Thanks for playing have a great day!"\
                                "Don't forget to save your data of this battle by clicking on the SAVE button as well!")
                
    elif uhealth < 1 and chealth > uhealth and not chealth < 1 :
        
        time.sleep(1)
        res = messagebox.askyesno("Results", "Oh no you have lost to your oponent, "\
                                "better luck nect time! Want to play again?")
        winner = "The computer :("
        
        if res == True:
            messagebox.showinfo("Results", "Head over to the first tab and choose a "\
            "new character to play with! Don't forget to save your data of this battle by clicking on the SAVE button as well!")
        else:
            messagebox.showinfo("Results", "Thanks for playing have a great day! "\
                                "Don't forget to save your data of this battle by clicking on the SAVE button as well!")
            
    elif uhealth < 1 and chealth < 1:
        
        winner = "No one :( Its a tie"
        res = messagebox.askyesno("Results", "Cool you tied! Want to play again?")
            
        if res == True:
            messagebox.showinfo("Results", "Head over to the first tab and choose "\
            "a new character to play with! Don't forget to save your data of this battle by clicking on the SAVE button as well!")
        else:
            messagebox.showinfo("Results", "Thanks for playing have a great day! "\
            "Don't forget to save your data of this battle by clicking on the SAVE button as well!")
        
    
# Setting up the characters and setting up varaibles depending on which
# character the user has selected

def character1():
    global chealth
    global uhealth
    
    # Method I researched online to find out how I could get text back from an alert 
    answer = simpledialog.askstring("Input", "I choose you! Perfect, now that you've choosen your pokemon, what will you name it?",
                                parent=window)
    charname.configure(text = answer, fg = "orange")
    charimg.configure(image = poke1img)
    
    # Assigns computer a character, character can not be the same as the users choice 
    player = 0
    randindex = random.randint(0, 2)
    
    # Keeps asigning the user a different character as long as the user and
    # the computer have the same character
    
    while player == randindex:
        randindex = random.randint(0, 2)
    
    comp.configure(text = characternames[randindex][0], fg = characternames[randindex][1])
    comp1img.configure(file = characterimages[randindex])
    
    messagebox.showinfo("Next Steps", "Perfect now head over to the 'Lets Play' tab to begin the math battle")
    
    style.configure("proggressbar.Horizontal.TProgressbar", background='orange')
    userbar["value"] = 100
    compbar["value"] = 100
    chealth = 100
    uhealth = 100
    comphealth.configure(text = 100)
    userhealth.configure(text = 100)

# same process as above is used if the 2 others characters are selected
def character2():
    global chealth
    global uhealth
    answer = simpledialog.askstring("Input", "I choose you! Perfect, now that"\
                        " you've choosen your pokemon, what will you name it?",
                                parent=window)
    charname.configure(text = answer, fg = "hot pink")
    charimg.configure(image = poke2img)
    
    player = 1
    randindex = random.randint(0, 2)
    
    while player == randindex:
        randindex = random.randint(0, 2)
        
    comp.configure(text = characternames[randindex][0], fg = characternames[randindex][1])
    comp1img.configure(file = characterimages[randindex])
    
    messagebox.showinfo("Next Steps", "Perfect now head over to the 'Lets Play' tab to begin the math battle")
    
    style.configure("proggressbar.Horizontal.TProgressbar", background='pink')
    userbar["value"] = 100
    compbar["value"] = 100
    chealth = 100
    uhealth = 100
    comphealth.configure(text = 100)
    userhealth.configure(text = 100)
    
def character3():
    global chealth
    global uhealth
    answer = simpledialog.askstring("Input", "I choose you! Perfect, now that you've "\
                                    "choosen your pokemon, what will you name it?",
                                parent=window)
    charname.configure(text = answer, fg = "blue")
    charimg.configure(image = poke3img)
    
    player = 2
    randindex = random.randint(0, 2)
    
    while player == randindex:
        randindex = random.randint(0, 2)
        
    comp.configure(text = characternames[randindex][0], fg = characternames[randindex][1])
    comp1img.configure(file = characterimages[randindex])
    
    messagebox.showinfo("Next Steps", "Perfect now head over to the 'Lets Play' tab to begin the math battle")
    
    style.configure("proggressbar.Horizontal.TProgressbar", background='blue')
    userbar["value"] = 100
    compbar["value"] = 100
    chealth = 100
    uhealth = 100
    comphealth.configure(text = 100)
    userhealth.configure(text = 100)

# process to save data: researched and learnt on my own
def fs():
    global winner
    
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    
    savedtext = "Great Battle! I hope that you had fun playing PokeAttack!\n \nHere is your game summary:\n Winner: "\
    + winner + "\n Your health: " + str(uhealth) + "\n Computer health: " + str(chealth)
    f.write(savedtext)
    f.close()
    
# Making the window 
window = Tk()
window.title("The PokeMath Attack")
window.geometry("1080x650")

# Tab Control
tab_control = ttk.Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text = "Select Your Character!")
tab_control.add(tab2, text = "Lets Play!")

# Title
title = Label(window, text = "The PokeMath Attack!", font=("Arial Bold", 20))
title.place(x = 380, y =100)

# Character Images
poke1img = PhotoImage(file="charizard.png")
poke1 = Label(tab1, image = poke1img)
poke1.pack(padx=50, pady=0, side=LEFT)

poke2img = PhotoImage(file="jiggly.png")
poke2 = Label(tab1, image = poke2img)
poke2.pack(padx=50, pady=0, side=LEFT)

poke3img = PhotoImage(file="squirt.png")
poke3 = Label(tab1, image = poke3img)
poke3.pack(padx=50, pady=0, side=LEFT)

# Initializing lists 
characterimages = ["charizard.png", "jiggly.png", "squirt.png"]
characternames = [["Charizard", "orange"], ["Jigglypuff", "hot pink"], ["Squirtle", "blue"]]
signs = ["+", "-", "*"]
damage = [1, 2, 5, 10, 25, 30, 50]

# Select Character
char1 = Button(tab1, text = "Charizard", bg = "orange", fg = "orange", command = character1)
char1.place(x = 80, y = 420, width = 200, height = 30)

char2 = Button(tab1, text = "Jigglypuff", fg = "hot pink", command = character2)
char2.place(x = 420, y = 420, width = 200, height = 30)

char3 = Button(tab1, text = "Squirttle", fg = "blue", command = character3)
char3.place(x = 720, y = 420, width = 200, height = 30)

# character display page 2
charname = Label(tab2, text = "", font=("Arial Bold", 15))
charname.place(x = 230, y =380)
charimg = Label(tab2, font=("Arial Bold", 15))
charimg.place(x = 170, y =150)

comp = Label(tab2, text = "", font=("Arial Bold", 15))
comp.place(x = 670, y =380)

# Showing the computer 
comp1img = PhotoImage()
comp1 = Label(tab2, image = comp1img)
comp1.place(x=580, y=160)

# Displaying the math question
howto = Label(tab2, text = "Get this question right to make your attack!", font=("Arial", 15))
howto.place(x = 180, y = 470)

getq = Button(tab2, text = "Click here to get your question", fg = "black", command = getquestion)
getq.place(x = 550, y = 465, width = 200, height = 30)

mathq = Label(tab2, text = "", font=("Arial Bold", 15))
mathq.place(x = 410, y = 500)

userinput = Entry(tab2, text = "Write Your Answer Here!", fg = "black")
userinput.place(x = 550, y = 500, width = 200, height = 30)

userinput.focus()

subq = Button(tab2, text = "Submit Answer!", fg = "black", command = check)
subq.place(x = 760, y = 465, width = 110, height = 65)

# Adding the progress bars
# computer progressbar
style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background='black')

# user progress bar
style = ttk.Style()
style.theme_use("default")
style.configure("proggressbar.Horizontal.TProgressbar", background='black')

save = Button(tab1, text = "save game data", fg = "black", command = fs)
save.place(x = 80, y = 465, width = 250, height = 50)

userbar = ttk.Progressbar( tab2, length = 200, style = "proggressbar.Horizontal.TProgressbar")

userbar.place(x = 200, y =420)

compbar = ttk.Progressbar( tab2, length = 200, style = "black.Horizontal.TProgressbar")

compbar.place(x = 620, y =420)

userhealth = Label(tab2, text = uhealth, font=("Arial Bold", 15))
userhealth.place(x = 410, y = 415)

comphealth = Label(tab2, text = chealth, font=("Arial Bold", 15))
comphealth.place(x = 830, y = 415)

tab_control.pack(expand = 1, fill = "both")
window.mainloop()
