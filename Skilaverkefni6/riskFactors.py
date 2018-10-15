import string

def read():
    try:
        filename = input("Enter filename containing csv data: ")
        with open(filename, 'r') as the_file:
            print("{:<33}{:<21}{:>6}      {:<15}{:>6}".format('Indicator', 'Min','', 'Max',''))
            counter_ = 0
            while counter_ < 87:
                print('-',end="")
                counter_ += 1
            print("")
            first_line = the_file.readline().split(',')
            fullfile = the_file.readlines()
            max_in(the_file, first_line, fullfile)
    except:
        print("Cannot find file {}".format(filename))
        print("{:<33}{:<21}{:>6}      {:<15}{:>6}".format('Indicator', 'Min','', 'Max',''))
        counter_ = 0
        while counter_ < 87:
            print('-',end="")
            counter_ += 1
        print("")
        return None

def max_in(the_file, first_line, fullfile):
    problems = ['Heart Disease Death Rate (2007)','Motor Vehicle Death Rate (2009)','Teen Birth Rate (2009)','Adult Smoking (2010)', 'Adult Obesity (2010)']
    for problem in problems:
        the_list = []
        i = first_line.index(problem)
        g = 0
        line_list = fullfile[0].split(',')
        while True:
            try:
                j = [float(line_list[i].strip('%')), line_list[0]]
            except:
                j = ['N/A', line_list[0]]
            the_list.append(j)
            try:
                line_list = fullfile[g].split(',')
                g += 1
            except:
                break
        max_it = max(the_list)
        min_it = min(the_list)
        printer(problem, max_it, min_it)

def printer(problem, max_it, min_it):
    max_state = max_it[1]
    max_count = max_it[0]
    min_state = min_it[1]
    min_count = min_it[0]
    problem += ':'
    print('{:<33}{:<21}{:>6.1f}      {:<15}{:>6.1f}'.format(problem, min_state, min_count, max_state, max_count,))



read()





