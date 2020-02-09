print("hello, welcome to PY++")
print("Please select your original code language")
print("A) Python to C++ \n B) About PY++ \n C) How to use it")
response = input(": "). lower()
if response == 'a':
    py = "print('banana')"
    cout = "cout>>"
    cin = "cin>>"
    coma = ['"', "'"]


    def findword(x, formatt):
        if formatt == "print":
            index = []
            indexNum = 0
            for word in x:
                if word == '(' or word == ")":
                    num = indexNum
                    index.append(num)
                indexNum = indexNum + 1
            slice_object = slice(index[0], index[-1] + 1, 1)
            return x[slice_object]
        elif formatt == "input":
            index = 0
            indexNum = 0
            for word in x:
                if word == "=":
                    index = indexNum

            indexNum = indexNum + 1
            slice_object = slice(0, index + 1, 1)
            return x[slice_object]
        elif formatt == "while":
            index = [0]
            """return while loop format = """
            indexState = 0
            indexCondi = []
            condiState = []
            indexNum = 0

            whileIndex = x.find('while') + 6
            colinIndex = x.find(':')
            condition = slice(whileIndex, colinIndex, 1)
            condiState.append(x[condition])

            slice_object = slice(colinIndex - 1, -1, 1)
            condiState.append(x[slice_object] + x[-1])
            return condiState


    # add two word together

    def addWord(file, py, formatt):
        if formatt == "print":
            return (cout + findword(file, formatt) + ';')
        elif formatt == "input":
            return (cin + findword(file, formatt) + ";")
        elif formatt == "while":
            condition = findword(file, formatt)
            state = []
            for line in py:
                if '\t' in line:
                    statement = findword(line, findFormat(line))
                    state.append(statement)

            return ("while (" + statement[0] + "){\n\r" + statement[1] + "\n}")
        elif formatt == "na":
            return "command not supported"


    # find the format

    def findFormat(statement):
        if "print" in statement:
            return "print"
        elif "input" in statement:
            return "input"
        elif "while" in statement:
            return "while"
        else:
            return "na"


    def getFile():
        file1 = open('py.txt', 'r')
        lines = file1.readlines()
        file1.close()
        return lines


    a = """print(thislist)
    thislist.remove("rambutan")
    print(thislist)
    thislist.pop()
    print(thislist)
    del thislist[0]"""

    py = getFile()
    print(py)

    for word in py:
        word = word.replace("\n", "")
        word = word.replace("\t", "")
        print(word)
        print(addWord(word, py, findFormat(word)))

    # print(getFile())
elif response == 'b':
    print("This is only a prototype for Blueprint 2020. \n Right now this program can only translate Input, Output and While loops from Python to C++. \n "
          "to use input you have to use 'x = input()'\n"
          "The purpose of the project it's make easier learning a new language. This program could be used for education and also for fun. \n"
          "Because that's a prototype function right now are limited, but our idea is to release to public and help everyone! ")
elif response == 'c':
    print("there is file name py.txt in the ssame folder, paste your code there")
else:
    print("Option not avalable")
