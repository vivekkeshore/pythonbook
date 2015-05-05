class Contacts(object):

    def __init__(self):
        self.data = dict()

    def add_contact(self, first, last, phone, email):
        self.data[first + ' ' + last] = first, last, phone, email

    def delete_contact(self, first, last):
        del self.data[first + ' ' + last]

    def print_names(self):
        for full_name, contact_details in self.data.items():
            self.print_contact(contact_details)
            print('--' * 15)

    def search_by_name(self, name):
        count = 0
        for contact_details in self.data.values():
            first, last = contact_details[0], contact_details[1]
            if first.find(name) != -1 or last.find(name) != -1:
                self.print_contact(contact_details)
                print('--')
                count += 1

        if count == 0:
            print('No results found')
        else:
            print('Found ' + str(count) + ' result(s)')

    def get_contact_by_full_name(self, full_name):
        contact_details = self.data.get(full_name)

        if contact_details:
            self.print_contact(contact_details)
        else:
            print('Contact does not exist')

    def print_contact(self, contact_details):
            print('Name:   ' + contact_details[0] + ' ' + contact_details[1])
            print('Phone:  ' + contact_details[2])
            print('E-mail: ' + contact_details[3])
