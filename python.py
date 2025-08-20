1.
 text = input("Nhập một chuỗi: ")
length = len(text)
print("Độ dài của chuỗi là:", length)

2.
s = input("Sample String: ")
freq = {}  # tạo dict rỗng
for char in s:              # duyệt từng ký tự
    if char in freq:        # nếu ký tự đã có trong dict
        freq[char] += 1     # tăng thêm 1
    else:
        freq[char] = 1      # nếu chưa có thì gán = 1
print("Kết quả:", freq)

3.
# Bài 3: Lấy 2 ký tự đầu và cuối của chuỗi
s = input("Sample String: ")
# Bỏ đi dấu nháy đơn hoặc nháy kép ở đầu/cuối nếu có
s = s.strip("'")
if len(s) < 2:
    print("Expected Result : Empty String")
else:
    result = s[:2] + s[-2:]
    print(f"Expected Result : '{result}'")

4.
# Bài 4: Thay ký tự đầu tiên bằng '$' (trừ lần xuất hiện đầu tiên)
s = input("Sample String: ")
# Bỏ dấu ngoặc đơn ' ở đầu và cuối
s = s.strip("'")
first_char = s[0]        # ký tự đầu tiên
rest = s[1:]             # phần còn lại
# thay thế các ký tự giống first_char trong rest thành '$'
rest = rest.replace(first_char, '$')
result = first_char + rest
print(f"Expected Result : '{result}'")

5.
# Bài 5: Swap 2 ký tự đầu của 2 chuỗi
s = input("Sample String: ")
# Tách chuỗi, bỏ ngoặc đơn và khoảng trắng
parts = [p.strip(" '") for p in s.split(",")]
s1, s2 = parts[0], parts[1]
# Đổi chỗ 2 ký tự đầu
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]
result = new_s1 + " " + new_s2
print(f"Expected Result : '{result}'")

6.
s = input("Sample String: ")
s = s.strip("'")
if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"
print(f"Expected Result : '{result}'")

7.
def not_poor_replace(text):
    pos_not = text.find("not")
    pos_poor = text.find("poor")
    if pos_not != -1 and pos_poor != -1 and pos_not < pos_poor:
        text = text[:pos_not] + "good" + text[pos_poor+4:]
    return text
print("Sample String : ", end="")
lines = []
while True:
    try:
        line = input()
        if line == "":  # Enter trống để dừng
            break
        lines.append(line)
    except EOFError:
        break
print("Expected Result :", end=" ")
for i, l in enumerate(lines):
    result = not_poor_replace(l)
    if i == 0:
        print(result)  # in cùng dòng với "Expected Result :"
    else:
        print(result)  # xuống dòng cho các câu tiếp theo

8.
def longest_word(words):
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest, len(longest)
# Nhập list từ, cách nhau bởi dấu phẩy
user_input = input("Sample output: ")
# Tách thành list
words_list = [w.strip() for w in user_input.split(",")]
# Gọi hàm
word, length = longest_word(words_list)
# In kết quả
print("Longest word:", word)
print("Length of the longest word:", length)

9.
def remove_char(s, n):
    # Xóa ký tự tại vị trí n
    return s[:n] + s[n+1:]
# Nhập chuỗi
text = input("Enter a string: ")
# Nhập vị trí index cần xóa
n = int(input("Enter the index to remove: "))
# Gọi hàm và in kết quả
result = remove_char(text, n)
print("Resulting string:", result)

10.
def exchange_first_last(s):
    return s[-1] + s[1:-1] + s[0]
# Nhập chuỗi từ người dùng
text = input("Sample String: ")
result = exchange_first_last(text)
print("Expected Result:", result)

11.
# Nhập chuỗi từ người dùng
s = input("Enter a string: ")
# Lấy các ký tự có chỉ số chẵn
result = s[::2]
print("New string:", result)

12.
# Nhập câu từ người dùng
sentence = input("Nhập một câu: ")
# Chuyển câu thành danh sách từ
words = sentence.split()
# Tạo dictionary để đếm
word_count = {}
for word in words:
    # Nếu từ đã có trong dictionary, tăng giá trị lên 1
    if word in word_count:
        word_count[word] += 1
    else:
        # Nếu chưa có, thêm từ vào dictionary với giá trị 1
        word_count[word] = 1
# In kết quả
print("Số lần xuất hiện của mỗi từ:")
for word, count in word_count.items():
    print(f"{word}: {count}")

13.
user_input = input("Nhập một chuỗi: ")
# Hiển thị chuỗi ở chữ hoa
print("Chuỗi in hoa:", user_input.upper())
# Hiển thị chuỗi ở chữ thường
print("Chuỗi in thường:", user_input.lower())

14.
# Nhập dãy từ người dùng
words = input("Nhập các từ, cách nhau bằng dấu phẩy: ")
# Tách thành danh sách từ
word_list = words.split(',')
# Loại bỏ từ trùng nhau và sắp xếp
distinct_sorted = sorted(set(word_list))
# Nối lại thành chuỗi cách nhau bằng dấu phẩy
result = ', '.join(distinct_sorted)
print("Kết quả:", result)

15.
def add_tags(tag, word):
    """
    Trả về chuỗi HTML với thẻ bao quanh và dấu nháy đơn ngoài cùng
    """
    return f"'<{tag}>{word}</{tag}>'"
# Ví dụ
print(add_tags('i', 'Python'))           # '<i>Python</i>'
print(add_tags('b', 'Python Tutorial'))  # '<b>Python Tutorial</b>'

16.
def insert_string_middle(original, word):
    """
    Chèn 'word' vào giữa hai ký tự đầu và cuối của chuỗi gốc.
    Giả sử chuỗi gốc có hai phần đối xứng ở đầu và cuối.
    """
    # Nếu chuỗi gốc dài hơn 2 ký tự, lấy nửa đầu và nửa cuối
    mid = len(original) // 2
    return original[:mid] + word + original[mid:]
# Ví dụ đúng
print(insert_string_middle('[[]]', 'Python'))  # [[Python]]
print(insert_string_middle('{{}}', 'PHP'))     # {{PHP}}

17.
def insert_end(s):
    """
    Trả về chuỗi gồm 4 lần lặp của 2 ký tự cuối cùng của s
    """
    if len(s) < 2:
        return "Chuỗi phải dài ít nhất 2 ký tự"
    last_two = s[-2:]  # lấy 2 ký tự cuối
    return last_two * 4  # lặp 4 lần
# Ví dụ
print(insert_end('Python'))     # onononon
print(insert_end('Exercises'))  # eseseses

18.
def first_three(s):
    """
    Trả về 3 ký tự đầu của s,
    nếu s ngắn hơn 3 ký tự thì trả về nguyên chuỗi
    """
    if len(s) < 3:
        return s
    return s[:3]
# Ví dụ
print(first_three('ipy'))      # ipy
print(first_three('python'))   # pyt

19.
# Define a variable 'str1' and assign it the value of the provided string.
str1 = 'https://www.w3resource.com/python-exercises/string'
# Use the rsplit() method with '/' as the separator to split the string from the right,
# and [0] to get the part before the last '/' character. Then, print the result.
print(str1.rsplit('/', 1)[0])  # Output: 'https://www.w3resource.com/python-exercises'
# Use the rsplit() method with '-' as the separator to split the string from the right,
# and [0] to get the part before the last '-' character. Then, print the result.
print(str1.rsplit('-', 1)[0])  # Output: 'https://www.w3resource.com/python

20.
def reverse_if_multiple_of_4(s):
    """
    Đảo ngược chuỗi s nếu độ dài của nó là bội số của 4.
    Nếu không, trả về chuỗi gốc.
    """
    if len(s) % 4 == 0:  # Kiểm tra bội số của 4
        return s[::-1]    # Đảo ngược chuỗi
    else:
        return s         # Trả về chuỗi gốc
# Ví dụ sử dụng
print(reverse_if_multiple_of_4("abcd"))       # "dcba" (độ dài 4)
print(reverse_if_multiple_of_4("hello"))      # "hello" (độ dài 5, không đảo)
print(reverse_if_multiple_of_4("Python1234")) # "4321nohtyP" (độ dài 10, không đảo)
print(reverse_if_multiple_of_4("12345678"))   # "87654321" (độ dài 8)

21.
def uppercase_if_2_in_first4(s):
    """
    Nếu trong 4 ký tự đầu của s có ít nhất 2 chữ hoa,
    chuyển toàn bộ chuỗi thành chữ hoa, ngược lại trả về chuỗi gốc.
    """
    # Lấy 4 ký tự đầu, đếm số chữ hoa
    first4 = s[:4]
    count_upper = sum(1 for c in first4 if c.isupper())
    
    if count_upper >= 2:
        return s.upper()  # Chuyển toàn bộ chuỗi thành chữ hoa
    else:
        return s          # Giữ nguyên chuỗi gốc
# Ví dụ sử dụng
print(uppercase_if_2_in_first4("PyThon"))  # "PYTHON" (2 chữ hoa trong 4 ký tự đầu)
print(uppercase_if_2_in_first4("Python"))  # "Python" (chỉ 1 chữ hoa trong 4 ký tự đầu)
print(uppercase_if_2_in_first4("JAVAscript"))  # "JAVASCRIPT" (3 chữ hoa trong 4 ký tự đầu)
print(uppercase_if_2_in_first4("java"))        # "java" (0 chữ hoa)

22.
def sort_lexicographically(s):
    """
    Trả về chuỗi được sắp xếp theo thứ tự từ điển.
    """
    return "".join(sorted(s))  # sorted(s) trả về list các ký tự đã sắp xếp, join lại thành chuỗi
# Ví dụ sử dụng
sample = "python"
print(sort_lexicographically(sample))  # "hnopty"
sample2 = "OpenAI"
print(sort_lexicographically(sample2))  # "AIOenp"

23.
def remove_newline(s):
    """
    Loại bỏ tất cả ký tự xuống dòng '\n' trong chuỗi.
    """
    return s.replace("\n", "")
# Ví dụ sử dụng
sample = "Hello\nWorld\nPython"
print(remove_newline(sample))  # "HelloWorldPython"

24.
def starts_with(s, prefix):
    """
    Kiểm tra xem chuỗi s có bắt đầu bằng prefix không.
    Trả về True nếu đúng, False nếu không.
    """
    return s.startswith(prefix)
# Ví dụ sử dụng
sample = "Python programming"
print(starts_with(sample, "Py"))    # True
print(starts_with(sample, "python")) # False (phân biệt chữ hoa/chữ thường)
print(starts_with(sample, "Java"))   # False

25.
def caesar_encrypt(text, shift):
    """
    Mã hóa Caesar: dịch từng ký tự trong text sang phải theo shift.
    Chỉ mã hóa các chữ cái, giữ nguyên các ký tự khác.
    """
    result = ""
    
    for char in text:
        if char.isupper():  # Chữ hoa
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():  # Chữ thường
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # Ký tự khác giữ nguyên
            result += char
    return result
# Ví dụ sử dụng
sample_text = "Hello, World!"
shift_amount = 3
encrypted = caesar_encrypt(sample_text, shift_amount)
print("Original:", sample_text)
print("Encrypted:", encrypted)  # "Khoor, Zruog!"

26.
import textwrap
text = """The Earth is the third planet from the Sun and the only 
astronomical object known to harbor life. About 71 percent 
of Earth's surface is covered with water, mostly by oceans."""
# Format văn bản với độ rộng 50 ký tự
formatted = textwrap.fill(text, width=50)
print(formatted)

27.
import textwrap
text = """   
        Python is a widely used high-level programming language.  
            It was created by Guido van Rossum in 1991.  
        Python emphasizes code readability and simplicity.  
"""
# Xóa khoảng trắng thụt đầu dòng
no_indent = textwrap.dedent(text)
print("Before:\n")
print(text)
print("After:\n")
print(no_indent)

28.
import textwrap
text = """Python is a powerful programming language.
It is easy to learn and fun to use.
Python supports multiple programming paradigms."""
# Thêm prefix ">> " vào mỗi dòng
with_prefix = textwrap.indent(text, prefix=">> ")
print(with_prefix)

29.
def indent_first_line(text, num_spaces=4):
    lines = text.splitlines()
    if not lines:  # nếu văn bản rỗng
        return text
    # thêm khoảng trắng vào dòng đầu
    lines[0] = " " * num_spaces + lines[0]
    return "\n".join(lines)
# Ví dụ
text = """Python is a widely used high-level programming language.
It emphasizes code readability and supports multiple paradigms.
Python was created by Guido van Rossum in 1991."""
result = indent_first_line(text, num_spaces=8)
print(result)

30.
# Một danh sách số ví dụ
numbers = [3, 3.1415926, 12.34567, 98.1, 7.9999]
print("Numbers with 2 decimal places:")
for n in numbers:
    print("{:.2f}".format(n))

31.
numbers = [3.14159, -7.5, 0, 12.0]
for n in numbers:
    print("{:+.2f}".format(n))

32.
numbers = [3.14159, -7.5, 12.99, 0]
for n in numbers:
    print("{:.0f}".format(n))

33.
numbers = [7, 85, 1234]
for n in numbers:
    print("{:05d}".format(n))

34.
numbers = [7, 85, 1234]
for n in numbers:
    print("{:*<5d}".format(n))

35.
n = 1234567890
print("{:,}".format(n))

36.
n = 0.756
print("{:.2%}".format(n))

37.
n = 123
print("{:<10}".format(n))  # trái
print("{:>10}".format(n))  # phải
print("{:^10}".format(n))  # giữa

38.
text = "Python is fun, and Python is powerful. Python rocks!"
print(text.count("Python"))

39.
text = "Python"
print(text[::-1])

40.
text = "Python is fun"
words = text.split()
reversed_text = " ".join(words[::-1])
print(reversed_text)

41.
text = "###Python is fun!!!###"
# Xóa ký tự '#' và '!' ở đầu/cuối
result = text.strip("#!")
print(result)

42.
from collections import Counter
text = 'thequickbrownfoxjumpsoverthelazydog'
counter = Counter(text)
for char, count in counter.items():
    if count > 1:
        print(char, count)

43.
import math
length = 34
width = 37
radius = 7
height = 8
area = length * width
volume = math.pi * radius * radius * height
print(f"The area of the rectangle is {area:.2f}cm\u00B2")
print(f"The volume of the cylinder is {volume:.3f}cm\u00B3")

44.
text = "w3resource"
for index, char in enumerate(text):
    print(f"Current character {char} position at {index}")

45.
import string
def contains_all_letters(s):
    return set(string.ascii_lowercase) <= set(s.lower())
text = "The quick brown fox jumps over the lazy dog"
print(contains_all_letters(text))

46.
text = "The quick brown fox jumps over the lazy dog."
words = text.split()
print(words)

47.
def lowercase_first_n(s, n):
    return s[:n].lower() + s[n:]
print(lowercase_first_n("PYTHONProgramming", 6))

48.
text = "32.054,23"
result = text.replace('.', 'X').replace(',', '.').replace('X', ',')
print(result)

49.
text = "Python is an amazing programming language"
vowels = "aeiou"
counts = {v: text.lower().count(v) for v in vowels}
for v, c in counts.items():
    if c > 0:
        print(v, c)

50.
text = "www.example.com/home/index.html"
parts = text.rsplit("/", 1)
print(parts)