import datetime
from Stack import Stack
from Task import Task

# Instantiating a Stack
pile = Stack()

# Instantiating some tasks
make_market = Task('Make Market ', 'Buy watermelon sugar, pineapple, rice, fish, cow meat ')
make_python_homework = Task('Python task ', 'Make Stack structure with Linked List and Python ')
make_piano_classes = Task('Piano Classes ', 'Watch and practice piano lessons ')
make_moto_race = Task('Moto Race ', 'Create event motocross race with lot mud ')
watch_python_classes = Task('Programming studies ', 'Learn python reading docs, watching classes, practice exercises ')

# Changing some attributes of these tasks
print('--------------------- Changing tasks attributes --------------------- \n')

# Changing market attributes
make_market.description += 'Increasing make market description.'
make_market.deadline = make_market.deadline + datetime.timedelta(days=10)
print(
    'Title: ' + make_market.title + '\n',
    'Deadline: ' + make_market.deadline.strftime('%d/%m/%Y, %H:%M:%S') + '\n'
)

# Changing watch_python_classes
watch_python_classes.title = 'Python stack task' + '\n'
watch_python_classes.deadline = watch_python_classes.deadline + datetime.timedelta(days=1, minutes=33, seconds=55)
print(
    'Title: ' + watch_python_classes.title,
    'Deadline: ' + watch_python_classes.deadline.strftime('%d/%m/%Y, %H:%M:%S') + '\n'
)

# Changing watch_python_classes
make_piano_classes.title = 'Defining new title'
make_piano_classes.description += 'i\' am really happy by learn piano'
make_piano_classes.deadline = watch_python_classes.deadline + datetime.timedelta(days=90, minutes=44, seconds=22)
print(
    'Title: ' + make_piano_classes.title + '\n',
    'Deadline: ' + make_piano_classes.deadline.strftime('%d/%m/%Y, %H:%M:%S') + '\n'
)

# Changing make_moto_race
make_moto_race.title += 'Increasing some new title' + '\n'
make_moto_race.description += '\U0001F6B2 \U0001F680 Make high sounds like RAM DAN DAN DAN DAN RAN DAN DAN DAN DAN \n'
make_moto_race.deadline = watch_python_classes.deadline + datetime.timedelta(days=11, minutes=60, seconds=5)
print(
    'Title: ' + make_moto_race.title,
    'Description: ' + make_moto_race.description,
    'Deadline: ' + make_moto_race.deadline.strftime('%d/%m/%Y, %H:%M:%S') + '\n\n'
)

# Stacking these tasks
pile.stack_up(make_market)
pile.stack_up(make_python_homework)
pile.stack_up(make_piano_classes)
pile.stack_up(make_moto_race)
pile.stack_up(watch_python_classes)

# Showing all registers of Stack
print('--------------------- Task at stack top --------------------- \n')
pile.show_register_on_pile_top()
print('------------------- Show all tasks on stack ------------------- \n')
pile.show_stack()

# Unstacking some tasks
print('--------------------- Unstack tasks --------------------- \n')
pile.unstack_from_top()
pile.show_register_on_pile_top()
pile.unstack_from_top()
pile.show_register_on_pile_top()

# Showing all registers of Stack
print('--------------------- Show Stack --------------------- \n')
pile.show_stack()

