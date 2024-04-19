import tkinter
import customtkinter as ct
from tkinter import messagebox
import pickle
import os




# Specify the directory where the pickled files are stored
directory = "E://Crop Recommendation"

# Load the machine learning model
with open(os.path.join(directory, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

# Load the MinMaxScaler
with open(os.path.join(directory, 'minmaxscaler.pkl'), 'rb') as f:
    mm = pickle.load(f)

# Load the StandardScaler
with open(os.path.join(directory, 'standardscaler.pkl'), 'rb') as f:
    sc = pickle.load(f)

# Define a function to perform prediction









ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

def predict():
    
    
    
    
    # Retrieve input values from text entry widgets
    global N, P, K, temperature, humidity, pH, rainfall
    
    N = int(N.get())
    P = int(P.get())
    K = int(Po.get())
    temperature = float(Temp.get())
    humidity = float(H.get())
    ph1 = float(ph.get())
    rainfall = float(R.get())
    
    print(N, P, K, temperature, humidity, ph1, rainfall)
    
    features = [N,P,K,temperature,humidity,ph1,rainfall]
    features_reshaped = np.array(features).reshape(1, -1)
    #MinMax Scaler
    mm_features = mm.transform(features_reshaped)
    #standard Sclar
    sc_features = sc.transform(mm_features)
    
    prediction = model.predict(sc_features).reshape(1,-1)
    
    value_to_find = prediction[0]
    keys_with_value = [key for key, value in data_dic.items() if value == value_to_find]
    if keys_with_value:
        
        ct.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"

        land= ct.CTk()
        land.wm_overrideredirect(True)
        def center_window(land, width, height):
            screen_width = land.winfo_screenwidth()
            screen_height = land.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            land.geometry('%dx%d+%d+%d' % (width, height, x, y))
            land.resizable(width=False,height=False)
        center_window(land, 400,200)
        land.title("Recommended Crop")


        def close():
            land.destroy()




        my_font1 = ct.CTkFont(family="Microsoft Sans Serif", size=30)
        my_font3 = ct.CTkFont(family="Microsoft Sans Serif", size=20)

        l2 = ct.CTkLabel(master=land, text=f"The Recommended crop is", font=('Microsoft Sans Serif', 28), text_color='black',width=400,height=23,fg_color=("white"),corner_radius=8)
        l2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        l2 = ct.CTkLabel(master=land, text=keys_with_value[0], font=('Microsoft Sans Serif', 28), text_color='purple',width=400,height=23,corner_radius=8)
        l2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button1 = ct.CTkButton(master=land,font=('Microsoft Sans Serif', 20) ,width=180,height=35,text="Close", command= close, corner_radius=6)
        button1.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)






        land.mainloop()

        
        
       
    else:
        print("No crop found for the given label:", value_to_find)
    
   
    
    
    
    
    
    







land= ct.CTk()
def center_window(land, width, height):
    screen_width = land.winfo_screenwidth()
    screen_height = land.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    land.geometry('%dx%d+%d+%d' % (width, height, x, y))
    land.resizable(width=False,height=False)
center_window(land, 1000,550)
land.title("Crop Recommendation")


my_font1 = ct.CTkFont(family="Microsoft Sans Serif", size=30)
my_font3 = ct.CTkFont(family="Microsoft Sans Serif", size=20)

text_var = tkinter.StringVar(value="Crop Recommendation ")



l2 = ct.CTkLabel(master=land, text="Crop Recommendation", font=('Microsoft Sans Serif', 28), text_color='#f2e9e4',width=400,
                               height=23,
                               fg_color=("white", "black"),corner_radius=8)
l2.place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)


#main frame
f1=ct.CTkFrame(land,width=1000,height=475,border_width=3,fg_color='#100c08',border_color='#100c08',corner_radius=10)
   
f1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
#company

mac1=ct.StringVar()

# N
# Entry for username
l2 = ct.CTkLabel(master=f1, text="Nitrogen", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)

N = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Nitrogen',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
N.place(relx=0.156, rely=0.2, anchor=tkinter.CENTER)


# P

l2 = ct.CTkLabel(master=f1, text="Phosphorus", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.45, rely=0.1, anchor=tkinter.CENTER)

P = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Phosphorus',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
P.place(relx=0.49, rely=0.2, anchor=tkinter.CENTER)

# Potassium

l2 = ct.CTkLabel(master=f1, text="Potassium", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.75, rely=0.1, anchor=tkinter.CENTER)

Po = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Potassium ',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
Po.place(relx=0.8, rely=0.2, anchor=tkinter.CENTER)

# Temperature

l2 = ct.CTkLabel(master=f1, text="Temperature", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.12, rely=0.4, anchor=tkinter.CENTER)

Temp = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Temperature ',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
Temp.place(relx=0.156, rely=0.5, anchor=tkinter.CENTER)

# Humidity 

l2 = ct.CTkLabel(master=f1, text="Humidity ", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.45, rely=0.4, anchor=tkinter.CENTER)

H = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Humidity ',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
H.place(relx=0.49, rely=0.5, anchor=tkinter.CENTER)

#pH

l2 = ct.CTkLabel(master=f1, text="Ph", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.72, rely=0.4, anchor=tkinter.CENTER)

ph = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Ph ',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
ph.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)


# Rainfall

l2 = ct.CTkLabel(master=f1, text="Rainfall", font=('Microsoft Sans Serif', 25), text_color='#f2e9e4')
l2.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)

R = ct.CTkEntry(master=f1,height=35, width=220, placeholder_text='Enter Rainfall ',bg_color="black",fg_color='#36454F',text_color='white',corner_radius=10,border_color='#36454F')
R.place(relx=0.159, rely=0.8, anchor=tkinter.CENTER)


button1 = ct.CTkButton(master=f1,font=('Microsoft Sans Serif', 20) ,width=180,height=40,text="Get Recommendation", command= predict, corner_radius=6)
button1.place(relx=0.6, rely=0.8, anchor=tkinter.CENTER)

land.mainloop()