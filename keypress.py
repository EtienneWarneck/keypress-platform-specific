try:
    import msvcrt

    def getKey():  # even though it's in a try block,
        # the function will be declared at a module scope.
        return msvcrt.getch()

# If not running on Windows:
except ImportError:

    # module defines functions for putting the tty into cbreak and raw modes.
    import sys
    # provides an interface to the POSIX calls for tty I/O control.
    import tty
    # termios provides an interface to the POSIX calls for tty I/O control.
    import termios

    def getkey():
        # fd file descriptor, returns INPUT which is 0
        fd = sys.stdin.fileno()
        # tcgetattr() gets the input and stores them in the termios structure.
        original_attributes = termios.tcgetattr(fd)

        try:
            # Put terminal into a raw mode and pass the input:
            tty.setraw(fd)
            # number of keypress read:
            ch = sys.stdin.read(3)
        finally:
            # tcsetattr() sets the parameters associated with the terminal from the termios structure:
            # TCSADRAIN Make the change occur after all output written to fd has been transmitted
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
            return ch


print(getkey())
