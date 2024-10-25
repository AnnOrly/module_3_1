calls = 0
def count_calls(calls):
    calls += 1

def string_info(string):
    global calls
    calls += 1
    print((len(string), string.upper(), string.lower()))

string_info('apple')
string_info('fruits')

def in_contains(string, list_to_search):
    global calls
    calls += 1

    if string in list_to_search:
        print(True)
    else:
        print(False)

in_contains('One', ['one', 'two', 'three'])
in_contains('tree', ['house', 'garden', 'dog'])

string_info('I_am_Нappy')

in_contains('pen', ['pencil', 'notebook'])

print(calls)