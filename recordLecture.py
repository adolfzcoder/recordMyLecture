import tkinter as tk
from tkinter import messagebox
import datetime
import os
import sounddevice
from scipy.io.wavfile import write
import webbrowser


CONFIG_FILE = "config.txt"

# Load the icon image


# Set#  the icon


def recLecture(seconds, moduleName, weekNum):
    if seconds == int(seconds):
        print("recording...")
        messagebox.showinfo("RECORDING", "Recording...")
        fps = 44100
        myRecording = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1)
        sounddevice.wait()
        moduleNameDirectory= moduleName.upper()
        current_time = datetime.datetime.now()

        timestamp = current_time.timestamp()
        write(f"{moduleNameDirectory}/{moduleName}_week{weekNum}_{timestamp}.wav", fps, myRecording)
        print("Done recording")
        
        messagebox.showinfo("SUCCESSFULLY RECORDED", f"Lecture successfully recorded. You can find it at {moduleNameDirectory}/{moduleName}_week{weekNum}_{timestamp}.wav")
    else:
        error('datatype')
        
        
def create_folders(module_names):
    for module_name in module_names:
        folder_name = module_name.upper()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            messagebox.showinfo("Folders Created", f"Folder '{folder_name}' created successfully.")


def update_config():
    with open(CONFIG_FILE, "w") as file:
        file.write("1")  # Update the config file to indicate that the script has been run


def is_first_run():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as file:
            file.write("0")  # Write a default value

        # Create the "courses.txt" file
        with open("courses.txt", "w") as courses_file:
            courses = [
                "BMC", "MCI", "DST", "ICG",
                "BSC", "PLU", "MTM", "IED", "APH", "AMC"
            ]
            for course in courses:
                courses_file.write(course + "\n")

        return True

    else:
        with open(CONFIG_FILE, "r") as file:
            line = file.readline().strip()
            if line == "0":
                # Create directories for each course
                with open("courses.txt", "r") as courses_file:
                    for course in courses_file:
                        course = course.strip()
                        folder_name = course.upper()
                        if not os.path.exists(folder_name):
                            os.makedirs(folder_name)
                return False

font = ("Arial", 18)
padx = 30
pady = 15
def howManyModules():
    root = tk.Tk()
    root.title("Number of Modules")
    
    label = tk.Label(root, text="How many modules do you have?")
    label.pack()
    
    entry = tk.Entry(root)
    entry.pack()
    
    def submit():
        try:
            module_quantity = int(entry.get())
            root.destroy()  
            return module_quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer value.")
    
    submit_button = tk.Button(root, text="Submit", command=submit, bg= "lightblue")
    submit_button.pack()
    
    root.mainloop()


def getAllModules(module_quantity):
    root = tk.Tk()
    root.title("Input All Modules")
    root.geometry("5000x500")  # Adjust window size as desired

    module_names = []

    def getModules():
        for entry in modules:
            module_names.append(entry.get())
        create_folders(module_names)
        update_config()
        root.destroy()

    # Create labels and entry fields with styling
    font = ("Arial", 18)
    padx = 30
    pady = 15

    modules = []
    for i in range(module_quantity):
        tk.Label(root, text=f"Module Name {i+1}:", font=font).grid(row=i, column=0, sticky="w", padx=padx, pady=pady)
        module = tk.Entry(root, font=font)
        module.grid(row=i, column=1, padx=padx, pady=pady)
        modules.append(module)

    # Create a submit button with styling
    submit_button = tk.Button(root, text="Add Modules", font=font, command=getModules)
    submit_button.grid(row=module_quantity, columnspan=2, padx=padx, pady=pady)

    root.mainloop()



def open_instagram():
    webbrowser.open("My Instagram","https://www.instagram.com/adolfzcoder/")

def open_github():
    webbrowser.open("https://github.com/adolfzcoder/")
def open_link(url):
    webbrowser.open(url)

def welcome_message():
    message = """Hi, Thank you for using this app. 
    I created this app because I wanted to record my lectures and have them stored in an organized manner. I thought others might be interested in using it as well. This app is completely free to use. If you end up liking it, please let me know through my Instagram or GitHub. Also, if you would like to contribute, you can contact me at adolfdavid17@gmail.com . Feel free to buy me a Kassie burger ;). Developed by A.David Technologies.
\n\n"""
    message += "For more information, visit my "
    message += " https://www.instagram.com/adolfzcoder/ OR "
    message += "https://github.com/adolfzcoder/"
    
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("WELCOME", message)

    root.bind("<Button-1>", lambda e: open_link("https://www.instagram.com/adolfzcoder/"))
    root.bind("<Button-2>", lambda e: open_link("https://github.com/adolfzcoder/"))
def main():

    if is_first_run():
        welcome_message()
        messagebox.showinfo("PS", "All the courses at NUST will be made as folders on your computer, simply delete the ones you are not doing. IF you are not from NUST then kindly contact me in order for me to make edits tailored for your insitiution (Add your institutions Modules to the app). If you are from NUST and your Subjects are not there, please contact me to add them")

    else:
        print("Script has been run before. Skipping module initialization.")

    root = tk.Tk()
    root.configure(bg="#333")  # Change "lightblue" to the color you prefer

    root.title("Auditory Learners")
    root.geometry("500x350")  # Adjust window size as desired

    
    # root.iconbitmap('icon.ico')  

    # Create entry widgets
    tk.Label(root, text="Module Name:", font=font, padx=padx, pady=pady, bg="lightblue").pack()
    module_name_entry = tk.Entry(root)
    module_name_entry = tk.Entry(root, width=20)
    module_name_entry.config(font=('Arial', 18))  # Set font size for better visibility
    module_name_entry.config(relief=tk.SOLID, bg="#ccc")     # Set border style
    module_name_entry.config(highlightthickness=2)
    module_name_entry.pack(pady=(0,10))

    tk.Label(root, text="Topic:", font=font, padx=padx, pady=pady, bg="lightblue").pack()
    week_num_entry = tk.Entry(root)
    week_num_entry = tk.Entry(root, width=20)
    week_num_entry.config(font=('Arial', 18))  # Set font size for better visibility
    week_num_entry.config(relief=tk.SOLID, bg="#ccc")     # Set border style
    week_num_entry.config(highlightthickness=2)
    week_num_entry.pack(pady=(0, 10))  # Add bottom padding only

    tk.Label(root, text="Lecture Length(Minutes):", font=font, padx=padx, pady=pady, bg="lightblue").pack()
    seconds_entry = tk.Entry(root, width=20)
    seconds_entry.config(font=('Arial', 18))  # Set font size for better visibility
    seconds_entry.config(relief=tk.SOLID, bg="#ccc")     # Set border style
    seconds_entry.config(highlightthickness=2) # Add a border
    seconds_entry.pack(pady=(0, 10))  # Add bottom padding only

    seconds_entry.pack()

    # Button to submit values
    def get_values():
        module_name = module_name_entry.get().upper()
        week_num = week_num_entry.get()
        seconds = int(seconds_entry.get()) * 60       #convert to minutes
        messagebox.showinfo("Values Retrieved", f"Module Name: {module_name}\nWeek Number: {week_num}\nDuration: {seconds/60} Minutes")
        recLecture(seconds, module_name, week_num) 
    submit_button = tk.Button(root, text="Submit", command=get_values, font=18, padx= 15, pady=10, bg = "lightblue")
    submit_button.pack()
    #icon_image = tk.PhotoImage(file="icon.png")
    # root.iconphoto(True, icon_image)
    root.mainloop()


def error(type):
    if type == 'datatype':
        messagebox.showinfo("DATATYPE ERROR", "Value(s) entered is not the right datatype, please try again. You might've entered a number value at a place which only accepts letters, eg 'How long to record lecture: '24'' rather do 'How long to record lecture: 24' ")
        exit()


if __name__ == "__main__":
    main()
