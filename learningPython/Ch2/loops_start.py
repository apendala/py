#
# Example file for working with loops
#

## Python only provides two ways to do loops - while & for.  Other languages have other ways

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x=x+1


  # define a for loop -- need to use RANGE or a list
  for x in range(5,10):
    print(x)


  # use a for loop over a collection
  days=['Mon', 'Tue', 'Wed', "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)
 
  # use the break and continue statements
  for x in range(5, 10):
    if(x==7):
      break
    print(x)

  for x in range(10, 20):
    if (x % 2 == 0):
      continue # stop executing rest of statements in loop and go back to for loop
    print(x)

  #using the enumerate() function to get index 
  days1=['Mon', 'Tue', 'Wed', "Thu", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days1):  ## enumerates the index AND value being looked at
    print(i, d)

if __name__ == "__main__":
  main()
