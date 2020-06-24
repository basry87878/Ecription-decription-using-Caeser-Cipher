def caesar(): #this function encrypt and decrypt the texts which the user input by ceaser ciper method.
	m = message.get()
	k = int(key_slider.get())
	if (var1.get())== 2:
		k = -k
	ciphertext = ''
	
	for symbol in m:

		if symbol.isalpha():                  # it make a condition that there are no spaces and digits in the string.
			num = ord(symbol) + k         #this will append the key value to the ordinary value of a letter
			
			if symbol.isupper():
				if   num > ord('Z'):  #this will encrypt the letters which is in captal letters 
					num -= 26
				elif num < ord('A'):  #this will decrypt the letters which is in captal letters
					num += 26

			elif symbol.islower():
				if   num > ord('z'):  #this will encrypt the letters which is in small letters
					num -= 26
				elif num < ord('a')  :#this will decrypt the letters which is in small letters
					num += 26
					

			ciphertext += chr(num)
		else:
			ciphertext += symbol

	result.delete(0.0, END)	    		      # clears 'Result' text box	
	result.insert(0.0, ciphertext ) 	      # prints the new 'ciphertext' in box Result
	return(ciphertext)
      	
from tkinter import *
menu=Tk()
menu.title('menu')
menu.geometry('500x500')

# Title label
instruction = Label(menu, text = "Caesar Cipher", font=("arial",17,"bold"))
instruction.grid(row = 1, column = 0, columnspan = 2, sticky = W)

# Method label
method = Label(menu, text = "Choose method:")
method.grid(row = 2, column = 0, columnspan = 2, sticky = W)

# Method options
var1 = IntVar()

option = Radiobutton(menu, text="Encrypt", pady = 5, variable=var1, value=1)
option.grid(row = 3, column = 0, columnspan = 1, sticky = W)

option = Radiobutton(menu, text="Decrypt", pady = 5, variable=var1, value=2)
option.grid(row = 3, column = 1, columnspan = 1, sticky = W)
# Message label
instruction = Label(menu, text = "Enter message: ")
instruction.grid(row = 4, column = 0, columnspan = 150, sticky = W)

# Message entry
message= Entry(menu)
message.grid(row = 5, column = 0, sticky = W)

# Key label
instruction = Label(menu, text = "Enter key (1-25): ")
instruction.grid(row = 6, column = 0, columnspan = 2, sticky = W)

#Key Slider
key_slider =Scale(menu, from_=1, to=25, orient=HORIZONTAL,length=200)
key_slider.grid(row = 7, column = 0, sticky = W)

# Submit 
submit_button = Button(menu, text = "Submit", command =caesar)
submit_button.grid(row = 8, column = 0, sticky = N)

# Result label
instruction = Label(menu, text = "Result", font=("arial",14,"bold"))
instruction.grid(row = 9, column = 0,columnspan = 2,sticky = W)

# Result 
result = Text(menu, width = 45, height = 6, wrap = WORD)
result.grid(row = 10, column = 0, columnspan = 3)

menu.mainloop()