## (incomplete) Solution to the Competition 2 by YouTube Channel - Coders Colony
## This is the driver code to the custom python library "letterMatrix.py" available at - https://github.com/shashankvray/Competitive-Programming/blob/main/letterMatrix.py

class coders_colony:
    def __init__(self, font_size, character):
        self.font_size = font_size
        self.character = character
    
    def clrscr(self):
        from os import system
        _ = os.system('cls')
        sleep(0.99)

    def print_menu(self):
        print("\n1. Show Clock\n2. Stopwatch\n3. Show Date\n4. Change font size (currently %s)\n5. Change font character (currently %s)\n6. Custom string\n7. Exit\n\n" %(self.font_size, self.character))

    #1
    def show_clock(self, font_size, character):
        while(True):
            try:
                now = datetime.datetime.now()
                print(now.strftime('%Y/%m/%d %I:%M:%S'))
                '''
                my_time = now.strftime('%Y/%m/%d %I:%M:%S')
                self.custom(font_size, character, my_time)
                '''
                sleep(0.99)
            except KeyboardInterrupt:
                self.print_menu()
                break

    #2
    def stopwatch(self, font_size, character, FwBw):
        if FwBw == 'b' or FwBw == 'B':
            given_time = input("Enter starting time in \"h:m:s\" format - ")
            
            while(given_time != "00:00:00"):
                print("Before - ", given_time, type(given_time))
                
                if type(given_time) == "<class 'datetime.timedelta'>":
                    given_time = datetime.datetime.strftime(given_time)
                given_time = datetime.datetime.strptime(given_time, '%H:%M:%S') - datetime.datetime.strptime('00:00:01', '%H:%M:%S')
                
                print("After - ", given_time, type(given_time))
                sleep(0.99)
        #strftime - Convert any object to a string 
        #strptime - Parse a string into a datetime object 
        
        elif FwBw == 'f' or FwBw == 'F':
            given_time = input("Enter final time in \"h:m:s\" format - ")
            while(datetime.datetime.strptime(datetime.datetime.strftime(given_time), '%H:%M:%S') != datetime.datetime.strftime(given_time)):
                given_time = (datetime.datetime.strptime('00:00:00', '%H:%M:%S') - datetime.datetime.strptime('00:00:00', '%H:%M:%S') + datetime.datetime.strptime('00:00:01', '%H:%M:%S')).time()
                print("f_TYPE == ",type(given_time))
        print(given_time, "\n")
        '''self.custom(font_size, character, custom_string)'''
        self.print_menu()
        pass
    
    #3
    def show_date(self, font_size, character):
        today_date = date.today().strftime("%d/%m/%Y")
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = days[datetime.datetime.today().weekday()]
        print(today_date, day)
        '''self.custom(font_size, character, today_date + day)'''
        self.print_menu()
    
    #4
    def foo_font_size(self, font_size):
        self.font_size = font_size
        print(type(self.font_size))
        self.print_menu()
    
    #5
    def foo_font_char(self, character):
        self.character = character
        self.print_menu()

    #6
    def custom(self, font_size, character, custom_string):
        print("\nCurrent Font Size: ", self.font_size, "\nCurrent Font Character: ", self.character, "\n")
        import letterMatrix
        others = {'0' : 'num_0', '1' : 'num_1', '2' : 'num_2', '3' : 'num_3', '4' : 'num_4', '5' : 'num_5', '6' : 'num_6', '7' : 'num_7', '8' : 'num_8', '9' : 'num_9'}
        
        #others = {0 : 'num_0', 1 : 'num_1', 2 : 'num_2', 3 : 'num_3', 4 : 'num_4', 5 : 'num_5', 6 : 'num_6', 7 : 'num_7', 8 : 'num_8', 9 : 'num_9'}
        
        for row in range(self.font_size):
            for i in custom_string:
                if i.isalpha():
                    getattr(letterMatrix, i.upper())(self.font_size, self.character, row)
                    print('  ', end = '')
                elif i.isnumeric():
                    getattr(letterMatrix, others[i])(self.font_size, self.character, row)
                    #others[i](self.font_size, self.character, row)
                    print('  ', end = '')
                else:
                    if ord(i) == 58: #:
                        letterMatrix.colon(self.font_size, self.character, row)
                    if ord(i) == 47: #/
                        letterMatrix.fw_slash(self.font_size, self.character, row)
                    if ord(i) == 92:
                        letterMatrix.bw_slash(self.font_size, self.character, row)
                    if ord(i) == 32: #SPACE
                        #letterMatrix.white_space(5)
                        print(' '*(5), end = '')
                    print('  ', end = '')
            print()       # AFTER ONE FULL ROW OF ALL CUSTOM CHARACTERS

if __name__ == '__main__':
    font_size = 10
    character = '*'
    obj = coders_colony(font_size, character)
    from datetime import date
    from datetime import datetime
    import datetime
    from time import sleep
    obj.print_menu()
    while(True):
        try:
            menu = int(input("Enter your menu choice: "))
        except ValueError:
            menu = 8
        if menu not in range(8):
            print("\nPlease enter a valid choice..\n")
            continue
        if menu == 1:
            obj.show_clock(font_size, character)
        if menu == 2:
            FwBw = input("Enter 'B' or 'b' for backward counting and \nEnter 'F' or 'f' for forward counting: ")
            obj.stopwatch(font_size, character, FwBw)
        if menu == 3:
            obj.show_date(font_size, character)
        if menu == 4:
            change = int(input("Enter new font size: "))
            if change < 5:
                print("I'm afraid everything would look clumsy.. Try a greater number!\n")
                obj.print_menu()
                continue
            obj.foo_font_size(change)
        if menu == 5:
            change = input("Enter new character: ")
            obj.foo_font_char(change)
        if menu == 6:
            change = input("Enter custom string: ")
            obj.custom(font_size, character, change)
        if menu == 7:
            print("Exiting..")
            exit()


