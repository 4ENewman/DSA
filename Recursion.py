
######################################### Building a call stack using iteration #########################################

def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while len(call_stack) != 0:
    return_value = call_stack[-1]
    call_stack.pop()
    print("Adding " + str(return_value))
    result += return_value["n_value"]
  print(call_stack)
  print(result)
  return result, call_stack

sum_to_one(4)

######################################### Iteration vs Recursion #########################################

def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result
 
sum_to_one(4)
# 10

def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n - 1)

print(sum_to_one(4))
# 10

######################################### Recursion Example #2 #########################################

def factorial(n):
  if n < 2:
    return n
  print("Recursing with input: {0}".format(n))
  return n * factorial(n - 1)

print(factorial(12))

######################################### Power Set Recursion #########################################

def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)

######################################### Recursion Example #3 #########################################

def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

######################################### Recursive Data Structures - Binary Search Trees #########################################

def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  #middle_idx = round(len(my_list) / 2)
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))
  tree_node = {"data": middle_value}
  #print(my_list[:middle_idx])
  #print(my_list[middle_idx + 1:])
  tree_node["left_child"] = build_bst(my_list[:middle_idx])
  tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])
  return tree_node

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

######################################### RECURSION VS. ITERATION #1 #########################################

# runtime: Linear - O(N)
def factorial(n):  
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)
 
factorial(3)
# 6
factorial(4)
# 24
factorial(0)
# 1
factorial(-1)
# ValueError "Input must be 0 or greater"



def factorial(n):
  total = 1
  if n >= 1:
    for num in range(n, 0, -1):
      total *= num
  return total

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)