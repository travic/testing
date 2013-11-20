print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\t\twhere there is none
"""

print "--------------"
print poem
print "--------------"


five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" %start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#Ended up mispselling crates on line 29 and noticed it after I couldnt figure out why line 32 wouldnt print ;). Refered to the read the script backwards meathod and figured it out in a few minutes xD. Progress???
