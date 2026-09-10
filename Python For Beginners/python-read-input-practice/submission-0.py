def add_two_numbers() -> int:
    input_line = input().strip()
    num1_str, num2_str = input_line.split(',')
    num1 = int(num1_str)
    num2 = int(num2_str)      
    result = num1 + num2    
    return result   

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
