print("\n=== SET EXAMPLE ===")
number={1,2,3,2,1} # duplicate remove automatically
print("Set:",number)
number.add(4)
number.discard(2)
print("New set:",number)
# set operation
even={2,4,6}
print("Union:",number | even)
print("Intersection:",number & even)