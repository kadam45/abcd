def accept_roll_numbers():
  """
  Accepts roll numbers of students and stores them in an array.
  """
  roll_numbers = []
  num_students = int(input("Enter the number of students: "))
  for i in range(num_students):
    roll_number = int(input("Enter roll number of student {}: ".format(i + 1)))
    roll_numbers.append(roll_number)
  return roll_numbers

def sort_roll_numbers(roll_numbers):
  """
  Sorts the roll numbers in ascending order using insertion sort.
  """
  for i in range(1, len(roll_numbers)):
    temp = roll_numbers[i]
    j = i - 1
    while j >= 0 and temp < roll_numbers[j]:
      roll_numbers[j + 1] = roll_numbers[j]
      j -= 1
    roll_numbers[j + 1] = temp

def linear_search(roll_numbers, target_roll_number):
  """
  Searches for a roll number in the given array using linear search.
  """
  for i in range(len(roll_numbers)):
    if roll_numbers[i] == target_roll_number:
      return i
  return -1

def sentinel_search(roll_numbers, target_roll_number):
  """
  Searches for a roll number in the given array using sentinel search.
  """
  roll_numbers.append(target_roll_number)
  for i in range(len(roll_numbers)):
    if roll_numbers[i] == target_roll_number:
      if i == len(roll_numbers) - 1:
        return -1
      else:
        return i
  return -1

# Main program
roll_numbers = accept_roll_numbers()
sort_roll_numbers(roll_numbers)

target_roll_number = int(input("Enter roll number to search for: "))

linear_search_result = linear_search(roll_numbers, target_roll_number)
sentinel_search_result = sentinel_search(roll_numbers, target_roll_number)

if linear_search_result == -1:
  print("Student with roll number {} did not attend the training program (Linear Search)".format(target_roll_number))
else:
  print("Student with roll number {} attended the training program (Linear Search)".format(target_roll_number))

if sentinel_search_result == -1:
  print("Student with roll number {} did not attend the training program (Sentinel Search)".format(target_roll_number))
else:
  print("Student with roll number {} attended the training program (Sentinel Search)".format(target_roll_number))