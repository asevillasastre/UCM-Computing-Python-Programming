"""
################################ PRACTICE 3 ###################################
"""

import py_compile

def get_functions(python_file, fun_data_file):
    """
    parameters:
    -----------
    python_file (file) as the file that will be read
    fun_data_file (file) as the file that will be written

    returns:
    --------
    If the sketch content in the file is syntactically correct,
    this function overwrites the contents of the "fun_data_file" file by typing:
    the names of the functions of "python_file" aligned to the left in a column of 30 spaces wide
    and the line numbers in which they appear aligned to the right in a column of 5 spaces wide

    If it is not syntactically correct, the function prints:
    <<python_file does not contain syntactically correct Python code>>
    """
    try:
        py_compile.compile(python_file, doraise=True)
        file = open(fun_data_file, "w")
        for element in my_own_sorted(python_file):
            file.write("{0:30}".format(element[0]))
            file.write("{0:>5}".format(element[1]))
            file.write("\n")
        #pylint warns that closing files << seems to have no effect >>
        file.close

    except py_compile.PyCompileError:
        print(python_file, "does not contain syntactically correct Python code")

def my_own_sorted(python_file):
    """
    parameters
    ----------
    python_file (file)

    returns
    -------
    A list of tuples with the names of the functions content in python_file ordered
    alphabetically following the ASCII code and the line in which they appear (list)
    """
    #This algorithm compares the first element of a list with the rest, exchanging them if one
    #should stay before the other
    #Until well ordered, it repeats the process for the rest of the elements
    lst = function_names(python_file)
    organized = 0
    while organized < len(lst):
        comparing = organized + 1
        while comparing < len(lst):
            for char in range(min(len(lst[comparing][0]), len(lst[organized][0]))):
                if lst[comparing][0][char] == lst[organized][0][char]:
                    char += 1
                elif lst[comparing][0][char] < lst[organized][0][char]:
                    lst[comparing], lst[organized] = lst[organized], lst[comparing]
                    break
                else:
                    break
            comparing += 1
        organized += 1
    return lst

def function_names(python_file):
    """
    parameters
    ----------
    python_file (file)

    returns
    -------
    A list of tuples that contain:
    the name of the functions of the file and the line number where they are (list)
    """
    result = []
    for element in def_searcher(python_file):
        start = 4 + element[2]
        while element[0][start] == " ":
            start += 1
        end = element[0].find("(")
        result.append((element[0][start:end], element[1]))
    return result

def def_searcher(python_file):
    """
    parameters
    ----------
    python_file (file)

    returns
    -------
    A list of tuples that contain:
    the content the line of code where a "def" is found, the number of such line,
    and the number of spaces that precede it (list)
    """
    lst, i = [], 0
    unitri_quotationmarks, bitri_quotationmarks = False, False
    for i in range(len(list_lines(python_file))):
        j = 0
        while list_lines(python_file)[i][j] == " ":
            j += 1
        comment = unitri_quotationmarks or bitri_quotationmarks
        if(list_lines(python_file)[i].find("def ", j), comment) == (j, False):
            lst.append((list_lines(python_file)[i], i+1, j))
        unitri_quotationmarks = read(i, unitri_quotationmarks, bitri_quotationmarks, python_file)[0]
        bitri_quotationmarks = read(i, unitri_quotationmarks, bitri_quotationmarks, python_file)[1]
    return lst

def list_lines(python_file):
    """
    parameters
    -----------
    python_file (file)

    returns
    -------
    A list with every line written in python_file as a string (list)
    """
    file = open(python_file, "r")
    lines = file.readlines()
    file.close
    #pylint warns that closing files << seems to have no effect >>
    return lines

def read(line, unitri_quotationmarks, bitri_quotationmarks, python_file):
    """
    parameters
    ----------
    python_file (file)
    line (int) as the line that is being checked
    unitri_quotationmarks and bitri_quotationmarks (booleans) indicate if the previous line
    is contained between triple single and double quotes, respectively


    returns
    --------
    A tuple with unitri_quotationmarks and bitri_quotationmarks (booleans) that indicate if the next
    line is contained between triple single and double quotes, respectively (tuple)
    """
    uni_quotationmarks, bi_quotationmarks, comment = 0, 0, False
    for element in specials_list(python_file):
        if element[0] == line and not (unitri_quotationmarks or bitri_quotationmarks):
            if (uni_quotationmarks % 2, bi_quotationmarks % 2, element[2]) == (0, 0, "#"):
                comment = True
            if not comment and element[2] == "'" and bi_quotationmarks % 2 == 0:
                uni_quotationmarks += 1
            if not comment and element[2] == '"' and uni_quotationmarks % 2 == 0:
                bi_quotationmarks += 1
            if not comment and element[2] == '"""':
                bitri_quotationmarks = not bitri_quotationmarks
            if not comment and element[2] == "'''":
                unitri_quotationmarks = not unitri_quotationmarks
        elif element[0] == line:
            if element[2] == "'''" and not bitri_quotationmarks:
                unitri_quotationmarks = not unitri_quotationmarks
            if element[2] == '"""' and not unitri_quotationmarks:
                bitri_quotationmarks = not bitri_quotationmarks
    return unitri_quotationmarks, bitri_quotationmarks

def specials_list(python_file):
    """
    parameters
    ----------
    python_file (file)

    returns
    -------
    A list of tuples that contain the line in which a special character appears,
    its corresponding column, and that special character as string (list)
    """
    #I added the characters in 3 statements to avoid an excessively long line
    lst = specials("#", python_file)
    lst = lst + specials('"', python_file) + specials("'", python_file)
    lst = lst + specials("'''", python_file) + specials('"""', python_file)
    return lst

def specials(string, python_file):
    """
    parameters
    ----------
    string (string) that will be searched
    python_file (file)

    returns
    -------
    A list of tuples with the occurrences of string in python_file, specifying in each one
    (the line, the column, the string), except cases in which this character is preceded
    by a backslash because then they are not read (list)
    """
    lst, i = [], 1
    for i in range(len(list_lines(python_file))):
        pos = list_lines(python_file)[i].find(string)
        add = pos != -1 and list(list_lines(python_file)[i])[pos-1] != "\\"
        if add:
            lst.append((i, pos, string))
        while add:
            pos = list_lines(python_file)[i].find(string, pos + 1)
            add = pos != -1 and list(list_lines(python_file)[i])[pos-1] != "\\"
            if add:
                lst.append((i, pos + 1, string))
    return lst
