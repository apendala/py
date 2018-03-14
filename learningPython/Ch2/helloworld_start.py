#
# Example file for HelloWorld
#

def main():
    print("hello world3")

# Check to see when this module has loaded, if __name__ has be assigned main, it means this
# file was launched at the command line or being explicitly invoked, so main should be called
# If this file was included in another file, you don't want the main() to be executed
if __name__ == "__main__":
    main()
