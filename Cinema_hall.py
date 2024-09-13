class Star_Cinema:
    __hall_list = []
    
    def _entry_hall(self,hall):
        Star_Cinema.__hall_list.append(hall)

    def view_all_halls(self):
        return Star_Cinema.__hall_list

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows =rows
        self.__cols = cols
        self.__hall_no = hall_no
        self._entry_hall(self)

    def get_hall_no(self):
        return self.__hall_no

    def entry_show(self,id,movie_name,time):
        tp = (id,movie_name,time)
        self.__show_list.append(tp)
        td_list = [['free' for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[id] = td_list
    
    def book_seats(self,id,seat_pos):
        if id not in self.__seats:
            print(f"ID {id} not found")
            return
        seating = self.__seats[id]
        for row,col in seat_pos:
            if 0<=row<self.__rows and 0<=col<self.__cols:
                if seating[row][col] == 'free':
                    seating[row][col] = 'booked'
                    print(f"Seat at row {row + 1}, col {col + 1} successfully booked.")
                else:
                    print(f"Seat at row {row + 1}, col {col + 1} is already booked.")
            else:
                print(f"Invalid seat position: row {row + 1}, col {col + 1}.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows are currently running.")
        else:
            print(f"Shows running in Hall {self.__hall_no}:")
            for show in self.__show_list:
                show_id, movie_name, time = show
                print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self,id):
        if id not in self.__seats:
            print(f"ID {id} not found")
            return
        
        seating = self.__seats[id]
        print(f'Available seat for {id}:')
        for row in seating:
            for seat in row:
                if seat == 'free':
                    print('0',end=' ')
                else:
                    print('1',end=' ')
            print()



hall1 = Hall(8,10,'H1')
hall1.entry_show('M1','The Conjuring','7:00 PM')
hall1.entry_show('M2','Smile','9:00 PM')
hall1.entry_show('M3','The Autopsy of Jane Doe','12:00 AM')

hall2 = Hall(10,10,'H2')
hall2.entry_show('M4','Searching' ,'10:00 AM')


while(True):
    print("\n1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    n = int(input('ENTER OPTION: '))
    if n == 4:
        break

    elif n == 1:
        for hall in Star_Cinema().view_all_halls():
            hall.view_show_list()

    elif n == 2:
        hall_no = input('Enter Hall No: ')
        id = input("Enter show id: ")

        found = False
        for hall in Star_Cinema().view_all_halls():
            if hall.get_hall_no() == hall_no:
                hall.view_available_seats(id)
                found = True
                break
        if not found:
            print(f"Hall {hall_no} not found.")

    elif n == 3:
        hall_no = input('Enter Hall No: ')
        id = input("Enter show id: ")
        seat_num = int(input("Enter number of seats to book: "))

        seat_pos = []
        for i in range(seat_num):
            row = int(input('Enter Row Number: ')) -1
            col = int(input('EnterColumn Number: ')) -1
            seat_pos.append((row,col))

        found = False
        for hall in Star_Cinema().view_all_halls():
            if hall.get_hall_no()==hall_no:
                hall.book_seats(id,seat_pos)
                found = True
                break
        if not found:
            print(f'Hall {hall_no} not found.')
    
    else:
        print("Invalid option. Please try again.")
        