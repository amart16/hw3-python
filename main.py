# Author: Alex Martin arm6554@psu.edu
def digit_sum(n):
  if n<= 0:
    return n
  else:
    return n%10 + digit_sum(n//10)
def print_n(s, n):
  if n <= 0:
    return
  else:
    print(s)
    return print_n(s, n-1)
def run():
  num = int(input("Enter an int: "))
  print(f"sum of digits of {num} is {digit_sum(num)}.")


if __name__ == "__main__":
    run()