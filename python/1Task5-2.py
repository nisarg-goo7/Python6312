def do_twice(f,arg):
	f(arg)
	f(arg)
def print_spam(arg):
	print arg
	print arg
do_twice(print_spam)