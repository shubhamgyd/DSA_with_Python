def isPalindrome(n):
  rev = 0
  temp = n

  while temp != 0:
    id = temp % 10
    rev = rev*10 + id
    temp = temp // 10
  return rev == n

if __name__ == "__main__":
  number = 4553
  print(isPalindrome(number))