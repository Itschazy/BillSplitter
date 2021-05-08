import random

class BillSplitter:
    def __init__(self):
        self.friends_list = {}
        self.number_of_participants = None
        self.total_bill = None
        self.lucky_person = None

    def input_data(self):
        print('Enter the number of friends joining (including you):')
        self.number_of_participants = int(input())

        if self.number_of_participants > 0:
            print('Enter the name of every friend (including you), each on a new line:')
            self.friends_list = {input(): 0 for i in range(self.number_of_participants)}
        else:
            return print('\nNo one is joining for the party')

        print('Enter the total bill value:')
        self.total_bill = int(input())
        self.add_bills()
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input()
        if answer == "Yes":
            self.lucky_one()
            self.number_of_participants -= 1
            self.calc_bills()
            self.add_bills()
            print(self.friends_list)
        else:
            print("No one is going to be lucky")
            print(self.friends_list)


    def lucky_one(self):
        self.lucky_person = random.choice(list(self.friends_list.keys()))
        print(f'{self.lucky_person} is the lucky one!')


    def calc_bills(self):
        return round(self.total_bill / self.number_of_participants, 2)

    def add_bills(self):
        for friend in self.friends_list.keys():
            if friend != self.lucky_person:
                self.friends_list[friend] = self.calc_bills()
            else:
                self.friends_list[friend] = 0

if __name__ == "__main__":
    test = BillSplitter()
    test.input_data()
