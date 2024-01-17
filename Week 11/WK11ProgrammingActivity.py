'''
Week 11 Team Activity: HR List (opening files)
Nicholas Wilkins
11/20/2023
'''
filename = "hr_system.txt"
# use with to open a file and store data in a variable (file object)
with open(filename) as file_var:
    # if the file has a header line, skip it 
    header = next(file_var) # header = file_var.readline() (other way to do this)
    # read each line, one by one, into a loop variable (for loop)
    for line in file_var:
        # strip whitespace from beginning and end of line if needed
        line = line.strip()
        # split the current line into parts (into a list)
        line_list = line.split(' ')
        # save different parts of the list into variables as needed
        name = line_list[0]
        id = line_list[1]
        title = line_list[2]
        salary = float(line_list[3])
        # do any calculations needed while still on a single line
        if title.lower() == 'engineer':
            paycheck = salary/24 + 1000
        else:
            paycheck = salary / 24
        # output (print) necessary items
        print(f'{name} (ID: {id}), {title} - ${paycheck:.2f}')
# any code we need to run after the file is closed