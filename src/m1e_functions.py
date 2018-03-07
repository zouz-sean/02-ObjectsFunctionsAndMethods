###############################################################################
#
# Read the code below. Trace (by hand) the execution of the code,
# predicting what will get printed.  Then run the code
# and compare your prediction to what actually was printed.
#
###############################################################################


def main():
    hello()
    goodbye()
    hello()
    hello()

    hello_and_goodbye()


def hello():
    print('Hello!  How are things?')


def goodbye():
    print('Goodbye!')
    print('   Ciao!')
    print('   Bai bai!')


def hello_and_goodbye():
    hello()
    goodbye()


main()
