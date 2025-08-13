#another exercise using functions from cbtnuggets course

def fun(name, location, year=2010):
    #from www.java2s.com
    nly = "%s/%s/%d" % (name, location, year)
    print(nly)
    return nly
    fullname = fun("Guido", "L.A.", 2004)
# This function takes a name, location, and an optional year (default is 2010)
fun(location="L.A.", year=2004, name="Guido")

rz = fun(location="L.A.", year=2004, name="Guido")
print(fullname)
