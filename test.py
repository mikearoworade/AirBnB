import re
import shlex

# # Search for a pattern in a string
# result = re.search(r'\b\w+@\w+\.\w+\b', 'Email me at john@example.com')
# print(result.group())  # Output: john@example.com

# # Find all occurrences of a pattern in a string
# matches = re.findall(r'\d+', 'There are 10 apples and 20 oranges')
# print(matches)  # Output: ['10', '20']

# # Replace occurrences of a pattern in a string
# new_string = re.sub(r'\bapples\b', 'bananas', 'I like apples and oranges')
# print(new_string)  # Output: I like bananas and oranges

# # Sample text containing email addresses
# text = "Contact me at john@example.com or jane@example.com"

# # Regular expression pattern to match email addresses
# pattern = r'\b\w+@\w+\.\w+\b'

# # Perform a search for the pattern in the text
# match = re.search(pattern, text)

# # If a match is found
# if match:
#     # Retrieve the matching substring
#     email = match.group()
#     print("Email found:", match)
# else:
#     print("No email found")


# # Sample text containing phone numbers
# text = "Contact me at 123-456-7890 or 987-654-3210"

# # Regular expression pattern to match phone numbers
# pattern = r'(\d{3})-(\d{3})-(\d{4})'

# # Perform a search for the pattern in the text
# match = re.search(pattern, text)
# matches = re.findall(pattern, text)

# # If a match is found
# if match:
#     # Retrieve the entire matched substring
#     phone_number = match.group()
#     print("Phone number found:", phone_number)
    
#     # Retrieve the substrings matched by each capturing group
#     area_code = match.group(1)
#     first_three_digits = match.group(2)
#     last_four_digits = match.group(3)
#     print("Area code:", area_code)
#     print("First three digits:", first_three_digits)
#     print("Last four digits:", last_four_digits)
# else:
#     print("No phone number found")

# if matches:
#     print(matches)al

line = 'User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {\'first_name\': "John", "age": 89})'
pattern = r'\(.*?\)'
parentheses = re.search(pattern, line) # search for parentheses
if parentheses:
    line_sub = re.sub(pattern, '', line) # Remove parentheses
    # print(line_sub)
    outside_parentheses = line_sub.split(".")
    outside_parentheses.reverse()
    # print(outside_parentheses) #1 args[0], args[1](<action>, <class>)

parentheses_values = re.findall(r'\((.*?)\)', line) # Search for id in parentheses
# print(parentheses_values)
clean_parentheses_value = re.sub(r'[\'"\[\]\\]', '', str(parentheses_values)) #remove quotes and brackets
# print(clean_parentheses_value)

curly_braces = re.findall(r'\{(.*?)\}', clean_parentheses_value)
if(curly_braces):
    # print(clean_parentheses_value.split(', '))
    id = []
    id.append(clean_parentheses_value.split(', ')[0]) # args[2] <id>
    clean_curly_braces = re.sub(r'[\'"\[\]]', '', str(curly_braces)) #remove quotes and brackets
    key_value_pairs =  clean_curly_braces.split(', ')
    for key_value_pair in key_value_pairs:
        each_key_value = key_value_pair.split(': ') # args[3], args[4](<key> <value>)
        args = outside_parentheses + id + each_key_value
        args = [int(i) if i.isdigit() else i for i in args]
        print(args)

else:
    inside_parentheses =  clean_parentheses_value.split(', ')
    # print(inside_parentheses) # args[2], args[3], args[4](<id>, <key>, <value>)
    if inside_parentheses == ['']:
        args = outside_parentheses
    else:
        args = outside_parentheses + inside_parentheses
    print(args)