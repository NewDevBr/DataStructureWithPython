from DataStructure.LinkedList.classes.phone import Phone
from DataStructure.LinkedList.classes.LinkedList import LinkedList


# Instantiating a linked list
phone_linked_list = LinkedList()

# Showing class methods
phone = Phone('Carlos', 18981113030, 'House number', "Street Yellow Ype")
phone.full_address = "Some address"
phone.name = "Carolina"
print(phone.name)
print(phone.full_address)
phone.number = 5518999766244
print(phone.number)
print(phone.full_address)


phone2 = Phone('Aline', 18981113030, 'House number', "Street Yellow Ype")
phone2.full_address = "Some address"
phone2.name = "Marta"
print(phone2.name)
print(phone2.full_address)

# Inserting data
phone_linked_list.insert_on_init('Carlos', 18981113030, 'House number', "Street Yellow Ype")
phone_linked_list.insert_on_init('Bia', 18981005050, 'Work number', "Saint Maria")
phone_linked_list.insert_on_init('Marcos', 18911115530, 'Work number', "Street Dark City")
phone_linked_list.insert_on_init('Carolina', 18988913030, 'Enterprise number', "Avenue John River")
phone_linked_list.insert(2, 'Bruno Andrade', 18971713550, 'Enterprise number', "Experience Avenue")
phone_linked_list.insert(3, 'Bianca', 18456556453, 'House number', "Highway to Hell DC")
phone_linked_list.insert(4, 'Jack', 1898111540, 'Work number', "Darkness Bread Highway")

# Showing list data
phone_linked_list.show()
phone_linked_list.item_at(3)
phone_linked_list.item_at(2)

# Deleting data
phone_linked_list.remove_from_init()
phone_linked_list.remove_random_register()
phone_linked_list.remove_random_register()

# Showing list data
phone_linked_list.show()
phone_linked_list.item_at(3)
phone_linked_list.item_at(2)
