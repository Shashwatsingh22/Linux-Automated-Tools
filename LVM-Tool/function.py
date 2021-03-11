from pyfiglet import Figlet

def render(text,style,num):
	f=Figlet(font=style)
	print('\n')
	print(f.renderText(text))

def sh_menu():
    print("""\t\t\t
                   Press 1: Create.
                   Press 2: Complete Detail.
                   Press 3: Specific.
                   Press 4: Exit.
                   \n
        Enter the Choice: """,end=" ")