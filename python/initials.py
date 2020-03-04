def abbrevName(name):
    return "{}.{}".format(name[0],name[(str.find(" ",name[0],len(name)))+1])


abbrevName("Jeremy Cunningham")
