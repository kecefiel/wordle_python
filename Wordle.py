import tkinter as tk
import random

def rgb_to_hex(): 
    '''Επιλεγει ενα τυχαιο χρωμα με τη μεθοδο rgb και το μετατρεπει στο δεκαεξαδικο συστημα'''
    r=random.randint(200,255) #Επιλέγονται τυχαία,με μορφή ακεραίου, τρεις τιμές από συγκεκριμένο εύρος τιμών
    g=random.randint(200,255)
    b=random.randint(200,255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)#Οι ακέραιοι μετατρέπονται σε έναν δεκαεξαδικό αριθμό όπου τα πρώτα δύο γράμματα
                                                #(ή αριθμοί) αναφέρονται στο κόκκινο, τα επόμενα δύο στο πράσινο και τα άλλα δύο στο μπλε

def create_board():
    '''#Δημιουργει τον πινακα του παιχνιδιου, που αποτελειται απο 6 γραμμες και 5 στηλες
    Σε καθε frame που δημιουργειται τοποθετειται ενα label στο οποιο τοποθετειται το γραμμα που πληκτρολογει ο χρηστης
    Εχει επισης δημιουργηθει η λιστα lb στην οποια έχουν ενσωματωθει ολα τα labels του πινακα ωστε να ειναι ευκολη η τροποποίησή τους'''
    for i in range (6):
        for j in range (1,6):
            window.configure(bg=color)
            frame=tk.Frame(master=window,relief=tk.SUNKEN,borderwidth=2,bg='white',height=6,width=6)#frame όπου τοποθετούνται τα labels
            frame.grid(row=i,column=j,padx=2,pady=2)
            label=tk.Label(master=frame,text='',bg=color,fg='BLACK',height=2,width=4)#labels όπου τοποθετούνται τα γράμματα
            label.grid(padx=5,pady=5,row=i,column=j)
            lb.append(label)# Προσθήκη των labels στη λίστα lb ώστε να διευκολύνεται η τοποθέτηση και διαγραφή γραμμάτων

def create_buttons():
    '''Δημιουργει τα γραμματα του πληκτρολογιου και τα κουμπια Delete, Backspace, Enter'''

    x1=45 #Συντεταγμενη πρωτης γραμμης
    x2=32 #Συντεταγμενη δευτερης γραμμης
    x3=63 #Συντεταγμενη τριτης γραμμης
    global keyboard
    keyboard=tk.Frame(window,width=500,height=121,bg=color) #Το Frame που περιεχει τα πληκτρα
    keyboard.place(x=53 , y=350)
    for j in range(3): #Για καθε γραμμη
        for i in range(len(l1[j])): #Για καθε γραμμα της καθε γραμμης
            b = tk.Button(keyboard,
                    text=l1[j][i], # Γραμμα απο τη λιστα
                    font=("Ariel", 8,'bold'),
                    fg='black',
                    bg='#e0ebeb',  #Αρχικο χρωμα
                    activebackground='#75a3a3', #Αρχικο χρωμα
                    activeforeground='black',
                    command= lambda letter_button=l1[j][i] : button_click(letter_button) , #Μεθοδος που καλειτε με το καθε πατημα
                    width='5',
                    height='2')

            if j==0: #Για τη πρωτη γραμμη συντεταγμενες πληκτρων
                b.place(x=x1, y=0)
                x1+=48 #Η αποσταση για το επομενο πληκτρο
            elif j==1:
                b.place(x=x2,y=41)
                x2+=48
            elif j==2:
                b.place(x=x3,y=82)
                x3+=48
            button.append(b) #Προσθηκη του καθε πληκτρου στη λιστα των κουμπιων

    delete_button=tk.Button(keyboard, text='Delete', command=delete, font=('London', 12, 'bold')) #Κουμπι διαγραφης ολης της σειρας-προσπαθειας
    delete_button.place(x=430, y=3)

    backspace_button=tk.Button(keyboard, text='Backspace', command=backspace, font=('London', 12, 'bold')) #Κουμπι διαγραφης του τελευταιου γραμματος
    backspace_button.place(x=400, y=85)

    enter_button=tk.Button(keyboard, text='Enter', command=enter, font=('London', 12, 'bold')) #Κουμπι ελεγχου λεξης
    enter_button.place(x=4, y=84)

def button_click(letter):
    '''Προσθηκη του γραμματος που πατηθηκε στο καταλληλο κουτι'''
    global guessN,letterN
    if letterN>4:return  #Ελεγχος πληροτητας γραμμης
    lb[guessN*5+letterN].configure(text=letter)  #Εμφανιση γραμματος στο καταλληλο κουτι
    guess[guessN]+=letter #Προσθηκη του γραμματος στην αντιστοιχη λεξη στον πινακα προσπαθειων
    letterN+=1 #Προχωραει στο επομενο κουτι της σειρα

def delete():
    '''Οριζει τον τροπο λειτουργιας του κουμπιου delete'''
    global guessN,letterN
    guess[guessN]='' #Μετατροπη της λεξης που αντιστοιχει στην καιρια προσπαθεια σε κενο
    for i in range(5):
        lb[guessN*5+i].configure(text='') #Μετατροπη του περιεχομενου του κουτιου σε κενο
    letterN=0 #επιστροφη στο πρωτο κουτι της σειρας

def backspace():
    '''Οριζει τον τροπο λειτουργιας του κουμπιου backspace'''
    global guessN,letterN
    if letterN>0:
        guess[guessN]=guess[guessN][:-1] #Κανει κενο το τελευταιο γραμμα που προστεθηκε στη λιστα
        lb[guessN*5+letterN-1].configure(text='') #Κανει κενο το τελευταιο κουτι
        letterN-=1 #Επιστροφη στο προηγουμενο κουτι της σειρας

def enter():
    '''Οριζει τον τροπο λειτουργιας του κουμπιου enter'''
    global guessN,letterN
    if guessN>5 :return #Ελεγχος αν εχουν τελειωσει οι προσπαθειες
    elif letterN<5: #Ελεγχος πληροτητας γραμμης
        letter_notification(letterN,'num_prob')
        return
    elif guess[guessN] not in dictio: #Αν η λεξη δεν υπαρχει στο λεξικο
        letter_notification('','not_in_dictionary')
        return
    getGuess(guess[guessN],guessN)  #Ελεγχος λεξης
    letterN=0  #Πηγαινει στη πρωτη στηλη κουτιων
    guessN+=1 #Πηγαινει στην επομενη γραμμη-προσπαθεια
    
def colorf(pressed_letter,color):
    '''Αλλαζει το χρωμα των πληκτρων στο πληκτρολογιο'''
    for b in button: #Αναζητηση του καταλληλου κουμπιου
        if not b.cget('text') == pressed_letter: pass
        else:
            if b.cget('bg')=='#66CD00':pass   #Αν το πληκτρο ειναι ηδη πρασινο δεν γινεται τιποτα
            elif b.cget('bg')=='#FF9912': #Αν το πληκτρο ειναι πορτοκαλι
                if color == 2: #Αλλαγη χρωματος μονο οταν γινεται πρασινο
                    b.configure(bg='#66CD00',activebackground='#52a600')#Πρασινο                              
            else: #Αν εχει το αρχικο χρωμα ή ειναι γκρι
                if color == 0:
                    b.configure(bg='#A1A1A1',activebackground='#7b7b7b')#Γκρι                
                    
                elif color == 1:
                    b.configure(bg='#FF9912',activebackground='#de7e00')#Πορτοκαλι
                elif color == 2:
                    b.configure(bg='#66CD00',activebackground='#52a600')#Πρασινο
                else:pass

def read_word():
    '''Ανοιγει τη λιστα των λεξεων και επιλεγει λεξεις μονο με 5 γραμματα και τις προσθετει στη λιστα word_five'''
    global word_five 
    word_five=[]
    with open('Words.txt','r',encoding="utf-8") as wordlist: 
             words=[ i for i in wordlist.readlines() ] #Λιστα με ολες τις λεξεις του αρχείου Words.txt
    for i in words:
            if len(i)==6: #Συνθήκη επιλογής των λέξεων με 5 γράμματα 
                    i=i.split()
                    word_five.extend(i) #Λιστα με λεξεις μονο 5 γραμματων 


def get_word():
    selected = random.choice(word_five)  #Επιλογή τυχαιας λέξης από την λίστα word_five με χρήση της βιβλιοθήκης random
    return selected


def correct_tonoi(wrong): 
    '''Διορθωση τονων'''
    tonoi={ "Ά" : "Α", "Έ" : "Ε", "Ή" : "Η", "Ί" : "Ι", "Ϊ" : "Ι", "΅Ι" : "Ι", "Ό" : "Ο","Ύ" : "Υ", "Ϋ" : "Υ", "΅Υ" : "Υ", "Ώ" : "Ω", "ς" : "Σ",}
    for letter in wrong:
        if letter in tonoi:
            wrong=wrong.replace(letter,tonoi[letter])
    return wrong

def dictionary(): 
    '''Λεξικο για αποδεκτες απαντησεις'''
    global dictio
    dictio=[]
    with open('Dictionary.txt','r',encoding="utf-8") as wordlist_dict:
        words_dict=[c.upper() for c in wordlist_dict.readlines()]
        for a in words_dict:
            a=str(a)
            a=correct_tonoi(a).upper() #Διόρθωση των τονων στο dictionary
            if len(a)==6: #Αποδοχη λεξεων με πεντε γραμματα
                a=a.split()
                dictio.extend(a) #Επεκταση λιστας με λεξεις με πεντε γραμματα

def color_board(color_list):
    '''Αλλαζει το background των label στον πίνακα'''
    for i,colorN in enumerate(color_list):       
        if colorN ==0:
            lb[(guessN)*5+i].configure(bg='#A1A1A1')
        if colorN ==1:
            lb[(guessN)*5+i].configure(bg='#FF9912')
        if colorN ==2:
            lb[(guessN)*5+i].configure(bg='#66CD00')
        

def getGuess(guess,guesses):
    global word,guessN
    if guesses < 6:
        colors=[]        
        if len(guess) == 5:
            for i, letter in enumerate(guess): #Το i αντιστοιχεί στην θέση και το letter στο γράμμα/στοιχείο της guess
                    if letter == word[i]: #Αν το letter είναι ίδιο με το αντίστοιχο γράμμα της word
                        u = 2
                        
                    if letter in word and not letter == word[i]: #Αν δεν είναι τα ίδια αλλά το letter υπάρχει στην word
                        u = 1
                       
                    if letter not in word:    #Αν το letter δεν υπάρχει στην word
                        u = 0
                        
                    colorf(letter,u)                     
                    colors.append(u)
                    if len(colors)==5:      
                        color_board(colors)
            if guess == word:
                create_win_popup()
            elif guesses==5:
                    create_lose_popup()
        

def letter_notification(num, exeption):
    '''Ειδοποιηση για μη εγκυρη λεξη '''
    if exeption == 'num_prob':
        if num==0:
             notification='Προσοχή! Δεν έχετε πληκτρολογήσει κάποιο γράμμα'
        elif num==1:
             notification='Προσοχή! Έχετε πλκτρολογήσει μόνο 1 γράμμα'
        else:
            notification=f'Προσοχή! Έχετε πληκτρολογήσει μόνο {num} γράμματα'
    elif exeption == 'not_in_dictionary':
        notification='Μη αποδεκτή λέξη'
    letter_number= tk.Label(window, text=notification, height=3, font=('London',10,'bold'))
    letter_number.place(x=300, y=180, anchor="center") 
    letter_number.after(2000, letter_number.destroy)     #Καταστροφη της ειδοποιησης μετα απο χρονικο διαστημα

    
def buttonPushed1():
    '''Κουμπι που τερματιζει το παιχνιδι αφου ο παικτης κερδισει'''
    win_popup.destroy()
    window.destroy()
    
def buttonPushed2():
    '''Κουμπι που τερματιζει το παιχνιδι αφου  ο παικτης χασει'''
    lose_popup.destroy()
    window.destroy()
                    
def create_win_popup():
    '''Οριζει την εμφανιση παραθυρου επιλογων οταν ο παικτης κερδισει. Δινεται η δυνατοτητα ειτε να παιξει ξανα ειτε να τερματισει το παιχνιδι'''
    global win_popup 
    win_popup = tk.Toplevel(window)
    win_popup.grab_set() #απενεργοποιείται το κεντρικό παράθυρο
    win_popup.resizable(height=False,width=False)
    win_popup.configure(bg=color)
    win_popup.geometry('200x200')
    win_popup.title('Τέλος Παιχνιδιού')
    b1_button= tk.Button(win_popup,text='Παίξε ξανά',font="london 10",command=play_again) 
    b1_button.place(x=15,y=110)
    b2_button= tk.Button(win_popup,text="Τερματισμός", font="london 10",command=buttonPushed1)
    b2_button.place(x=110,y=110)
    tk.Label(win_popup,text="Συγχαρητήρια :)",bg=color,fg="black",font='london').pack(fill="x")
    tk.Label(win_popup,text="Βρήκες τη λέξη:",bg=color,fg="black",font='london').pack(fill="x")
    tk.Label(win_popup,text=word,bg=color,fg="black",font='london 20').pack(fill="x")
    win_popup.mainloop()
    
def create_lose_popup():
    '''Οριζει την εμφανιση παραθυρου επιλογων οταν ο παικτης χασει.'''
    global lose_popup
    lose_popup =tk.Toplevel(window)
    lose_popup.grab_set()
    lose_popup.resizable(width=False, height=False)
    lose_popup.configure(bg=color)
    lose_popup.geometry('200x200')
    lose_popup.title('Τέλος Παιχνιδιού')
    b3_button=tk.Button(lose_popup,text='Προσπάθησε ξανά',font="london 10",command=try_again)
    b3_button.place(x=15,y=60)
    b4_button= tk.Button(lose_popup,text='Παίξε ξανά',font="london 10",command=play_again) 
    b4_button.place(x=15,y=90)
    b5_button= tk.Button(lose_popup,text="Τερματισμός", font="london 10",command=buttonPushed2)
    b5_button.place(x=15,y=120)
    tk.Label(lose_popup,text="Έχασες :(",bg=color,fg="black",font=('london',15)).pack(fill="x")
    lose_popup.mainloop()


def play_again():
    '''Αρχη νεου γυρου (εκαθαριση πινακα, χρωματων και επιλογη νεας λεξης)'''
    global letterN,guessN,guess,word
    letterN=0
    guessN=0
    guess=['','','','','','']
    win_conf() #Αλλαγη χρωματων του background
    for i in lb: #Καθε κουτι γινεται κενο
         i.configure(text='', bg=col)
    for b in button: #Καθε πληκτρο παιρνει το αρχικο του χρωμα
        b.configure(bg='#e0ebeb')
        b.configure(activebackground='#75a3a3')
    try:
        win_popup.destroy()
    except:
        lose_popup.destroy()
        reveal_word() #Εμφανιση λεξης του προηγουμενου γυρου
    word = get_word().upper() #Επιλογη νεας λεξης
    #print(word) #Εμφανιζει τη λεξη του γυρου

def win_conf():
'''Εφόσον ο παίκτης επιλέξει να παίξει καινούριο παιχνίδι, το παράθυρο αλλάζει χρώμα με τη χρήση της συνάρτησης rgb_to_hex'''
    global col,keyboard
    col=rgb_to_hex()#Επιλέγεται τυχαία νέο χρώμα από τη συνάρτηση rgb_to_hex
    window.configure(bg=col)#Το παράθυρο,το emptybox,το background του label 'Wordle' και το background του πληκτρολογίου αποκτούν
    emptybox.configure(bg=col) #Το νέο χρώμα που ορίστηκε από τη συνάρτηση rgb_to_hex
    wl.configure(bg=col)
    keyboard.configure(bg=col)

def try_again():
    '''#Εφόσον ο παίκτης χάσει, του δίνεται η δυνατότητα να προσπαθήσει πάλι να βρει τη ζητούμενη λέξη
    Και σε αυτή την περίπτωση τα γράμματα σβήνονται, όμως ο πίνακας δεν αλλάζει χρώμα'''
    global letterN,guessN,guess,word
    letterN=0
    guessN=0
    guess=['','','','','','']
    for i in lb:
         i.configure(text='', bg=color)#Διαγράφονται τα γράμματα από τα labels και το χρώμα τους γίνεται ίδιο με αυτό του παραθύρου
    for b in button:
        b.configure(bg='#e0ebeb')#Τα buttons επιστρέφουν στο αρχικό τους χρώμα
        b.configure(activebackground='#75a3a3')#Το active background επιστρέφει στο αρχικό χρώμα
    lose_popup.destroy()
    
    
def reveal_word():
    '''#Όταν ο παίκτης,αφού χάσει, επιλέξει να παίξει καινούριο παιχνίδι, αποκαλύπτεται η προηγούμενη ζητούμενη λέξη
    Δημιουργείται το label reveal_word αποκαλύπτοντας τη λέξη και στη συνέχεια εξαφανίζεται μετά από περίπου 3 δευτερόλεπτα'''
    reveal_word= tk.Label(window, text=word,font=('London',12,'bold'))
    reveal_word.place(x=270, y=130) 
    reveal_word.after(2000, reveal_word.destroy)           

#Κυρίως πρόγραμμα    
lb=[]#Λίστα που περιέχει όλα τα labels του πίνακα
guess=['','','','','','']    #Πινακας στον οποιο θα προστεθουν τα γραμματα που πληκτρολογουνται 
guessN=0   #Αριθμος της γραμμης κουτιων- της προσπαθειας
letterN=0 #Αριθμος του  κουτιου τη γραμμης-γραμματος της λεξης
l1=['ΕΡΤΥΘΙΟΠ','ΑΣΔΦΓΗΞΚΛ','ΖΧΨΩΒΝΜ']  #Λιστα των γραμματων ανα σειρα με τη σειρα του πληκτρολογιου 
button=[]  # Λιστα που θα προστεθουν τα πληκτρα
read_word()
word = get_word().upper() # Word--> επιλεγμένη λέξη
#print(word) #Εμφανιζει τη λεξη του γυρου
guesses = 0
dictionary()
window=tk.Tk()#Κυρίως παράθυρο του παιχνιδιού
window.title('Wordle')#Τίτλος κυρίως παραθύρου
window.geometry('600x700')#Διαστάσεις κυρίως παραθύρου
window.resizable(width=False, height=False)
color=rgb_to_hex()#Μεταβλητή οπου εκχωρειται η τιμη της συναρτησης rgb_to_hex
emptybox=tk.Label (window,height=3,width=22,bg=color)#Κενό παραλληλόγραμμο που βοηθά στην τοποθέτηση του πίνακα στο κέντρο του παραθύρου
emptybox.grid()
wl=tk.Label(window,text='Wordle',bg=color,font=('London',22, 'bold'))#label που αναγράφει το όνομα του παιχνιδιού
wl.place(x=8,y=2)
create_board()
create_buttons()
window.mainloop()
