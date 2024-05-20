#!/usr/bin/python3

if __name__ == "__main__":
    filename = "2.csv"
    username = "Ervin Howell"
    id = 2
    with open(filename, 'r') as f:
        for line in f:
            if not line == '\n':
                if not str(id) in line:
                    print("User ID: Incorrect / ", end='')
                    flag = 1
                if not str(username) in line:
                    print("Username: Incorrect")
