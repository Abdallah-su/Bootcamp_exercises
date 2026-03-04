# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number.
#  When instantiating an object create an attribute called call_history 
# which value is an empty list.



class Phone:
    def __init__(self, phone_number):
        self.phone_num =phone_number
        self.call_history = [ ]
        self.message = [ ]

# Add a method called call that takes both self and other_phone 
# (i.e another Phone object) as parameters. 
# The method should print a string stating who called who,
#  and add this string to the phone’s call_history.

    def call(self, other_phone):
        if self.phone_num != other_phone:
            self.call_history.append(other_phone)
        print(f'{other_phone } call {self.phone_num}')

# Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self):
        print(f' call history: {self.call_history}')

# Add another attribute called messages to your __init__() method 
# which value is an empty list.

# Create a method called send_message which is similar to the call method.
# Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content
    def send_message(self, other_phone):
      info1 = {'to': other_phone}
      self.message.append(info1)
      info2 ={'from': self.phone_num}
      self.message.append(info2)
      return self.message


         
    def show_incoming_messages(self):
        print(f'message: {self.message[0]}')

    def show_outgoing_messages(self):
        print(f'message: {self.message[1]}')

    
# Create the following methods: show_outgoing_messages(self),
#  show_incoming_messages(self), show_messages_from(self)

# Test your code !!!

my_phone = Phone('02326378')
my_phone.call('0283847')
my_phone.show_call_history()
my_phone.send_message('0283847')
my_phone.show_incoming_messages()
my_phone.show_outgoing_messages()