# In my last program i had made password generator now I extending it
# to a GUI based application
import random
import tkinter

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeric_character = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_']


def password_generator(no_of_letters, no_of_numbers, no_of_symbols):
    no_of_letters1 = no_of_letters.get()
    no_of_numbers1 = no_of_numbers.get()
    no_of_symbols1 = no_of_symbols.get()
    # int(no_of_symbols)
    # int(no_of_letters)
    # int(no_of_numbers)
    password = []
    for i in range(0, no_of_letters1):
        password.append(random.choice(alphabets))
    for i in range(0, no_of_numbers1):
        password.append(random.choice(numeric_character))
    for i in range(0, no_of_symbols1):
        password.append(random.choice(symbols))
    random.shuffle(password)
    final_password = ""
    for i in password:
        final_password += i
    return final_password


def display():
    password = password_generator(number_of_letters, number_of_number, number_of_symbols)
    output.set(password)


main_window = tkinter.Tk()
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=0)
main_window.rowconfigure(2, weight=0)
main_window.rowconfigure(3, weight=0)
main_window.rowconfigure(4, weight=1)
main_window.rowconfigure(5, weight=0)
main_window.rowconfigure(6, weight=2)
main_window.rowconfigure(7, weight=0)
main_window.rowconfigure(8, weight=3)
main_window.title("Password Generator")
main_window.geometry('530x250-8-200')
main_window.resizable(False,False)


Label_no_of_letters = tkinter.Label(main_window, width=30, text="Enter the number of letters req:")
Label_no_of_letters.grid(row=1, column=0, sticky='nsew')

number_of_letters = tkinter.IntVar()
entry_no_of_letters = tkinter.Entry(main_window, width=20, textvariable=number_of_letters)
entry_no_of_letters.grid(row=1, column=3, sticky='nsew', columnspan=5)

Label_no_of_numbers = tkinter.Label(main_window, width=30, text="Enter the number of numbers req:")
Label_no_of_numbers.grid(row=2, column=0, sticky='nsew')

number_of_number = tkinter.IntVar()
entry_no_of_numbers = tkinter.Entry(main_window, width=25, textvariable=number_of_number)
entry_no_of_numbers.grid(row=2, column=3, sticky='nsew', columnspan=5)

# number_of_number1 = int(number_of_number)

Label_no_of_symbols = tkinter.Label(main_window, width=30, text="Enter the number of symbols req:")
Label_no_of_symbols.grid(row=3, column=0, sticky='nsew')

number_of_symbols = tkinter.IntVar()
entry_no_of_symbols = tkinter.Entry(main_window, width=25, textvariable=number_of_symbols)
entry_no_of_symbols.grid(row=3, column=3, sticky='nsew', columnspan=5)

# number_of_symbols1 = int(number_of_symbols)

output = tkinter.StringVar()

LabelOutput = tkinter.Label(main_window, text="Password generated:")
LabelOutput.grid(row=5, column=0, sticky='nsew')

output_window = tkinter.Entry(main_window, textvariable=output)
output_window.grid(row=5, column=3, sticky='nsew', columnspan=5)

GenerateButton = tkinter.Button(main_window, text="GENERATE", command=display)
GenerateButton.grid(row=7, column=0, sticky='nsew', columnspan=10)

main_window.mainloop()
