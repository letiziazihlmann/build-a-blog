def get_initials(fullname):
    namelist = fullname.split()
    init = ''
    for aname in namelist:
        initials = aname[0]
        init = init + initials.upper()
    return init
def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
