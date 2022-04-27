# Задача №3 из урока 2. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import sys
import ctypes
import struct

def show_size(x, level=0):
    print('\t' * level, f'id= {id(x)}, type= {x.__class__}, size= {sys.getsizeof((x))}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

# 1 вариант решение через числовые операции
num = int(input('Введите число = '))
result = 0
show_size(num)
print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
print('\t', struct.unpack('LLLbb', ctypes.string_at(id(num), sys.getsizeof(num))))
show_size(result)
print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
print('\t', struct.unpack('LLL', ctypes.string_at(id(result), sys.getsizeof(result))))
while num > 0:
    result = num % 10 + result * 10
    num = num // 10
print('Обратное число = ', result)
show_size(num)
print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
print('\t', struct.unpack('LLL', ctypes.string_at(id(num), sys.getsizeof(num))))
show_size(result)
print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
print('\t', struct.unpack('LLLL', ctypes.string_at(id(result), sys.getsizeof(result))))

# Введите число = 12345
#  id= 5452176, type= <class 'int'>, size= 14, object= 12345
# 	 b'\x01\x00\x00\x00(AF\\\x01\x00\x00\x0090'
# 	 (1, 1548108072, 1, 57, 48)
#  id= 1548199840, type= <class 'int'>, size= 12, object= 0
# 	 b'\xd5\x00\x00\x00(AF\\\x00\x00\x00\x00'
# 	 (213, 1548108072, 0)
# Обратное число =  54321
#  id= 1548199840, type= <class 'int'>, size= 12, object= 0
# 	 b'\xd5\x00\x00\x00(AF\\\x00\x00\x00\x00'
# 	 (213, 1548108072, 0)
#  id= 5349408, type= <class 'int'>, size= 16, object= 54321
# 	 b'\x01\x00\x00\x00(AF\\\x02\x00\x00\x001T\x01\x00'
# 	 (1, 1548108072, 2, 87089)


# 2 вариант решение через строку
# num = input('Введите число = ')
# result = ''
# show_size(num)
# # print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
# # print('\t', struct.unpack('LLLLLi' + 'c' * 6, ctypes.string_at(id(num), sys.getsizeof(num))))
# show_size(result)
# # print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
# # print('\t', struct.unpack('LLLLli' + 'c', ctypes.string_at(id(result), sys.getsizeof(result))))
# for i in num:
#     result = i + result
# print('Обратное число = ', result)
# show_size(num)
# # print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
# # print('\t', struct.unpack('LLLLLi' + 'c' * 6, ctypes.string_at(id(num), sys.getsizeof(num))))
# show_size(result)
# # print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
# # print('\t', struct.unpack('LLLLli' + 'c' *  6, ctypes.string_at(id(result), sys.getsizeof(result))))

# Введите число = 12345
#  id= 5925024, type= <class 'str'>, size= 30, object= 12345
# 	 b'\x01\x00\x00\x000n\x86\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x00\x00\x00\x00\x00\x00\x0012345\x00'
# 	 (1, 1552313904, 5, 4294967295, 228, 0, b'1', b'2', b'3', b'4', b'5', b'\x00')
#  id= 3939040, type= <class 'str'>, size= 25, object=
# 	 b'<\x00\x00\x000n\x86\\\x00\x00\x00\x00\x00\x00\x00\x00\xe5\x00\x00\x00\x00\x00\x00\x00\x00'
# 	 (60, 1552313904, 0, 0, 229, 0, b'\x00')
# Обратное число =  54321
#  id= 5925024, type= <class 'str'>, size= 30, object= 12345
# 	 b'\x01\x00\x00\x000n\x86\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x00\x00\x00\x00\x00\x00\x0012345\x00'
# 	 (1, 1552313904, 5, 4294967295, 228, 0, b'1', b'2', b'3', b'4', b'5', b'\x00')
#  id= 5965088, type= <class 'str'>, size= 30, object= 54321
# 	 b'\x01\x00\x00\x000n\x86\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x1a<\x00\x00\x00\x00\x0054321\x00'
# 	 (1, 1552313904, 5, 4294967295, 3939044, 0, b'5', b'4', b'3', b'2', b'1', b'\x00')


# 3 вариант
# num = input('Введите число = ')
# result = ''
# show_size(num)
# print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
# print('\t', struct.unpack('LLLLLi' + 'c' * 6, ctypes.string_at(id(num), sys.getsizeof(num))))
# show_size(result)
# print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
# print('\t', struct.unpack('LLLLli' + 'c', ctypes.string_at(id(result), sys.getsizeof(result))))
# result = num[::-1]
# print('Обратное число = ', result)
# show_size(num)
# print('\t', ctypes.string_at(id(num), sys.getsizeof(num)))
# print('\t', struct.unpack('LLLLLi' + 'c' * 6, ctypes.string_at(id(num), sys.getsizeof(num))))
# show_size(result)
# print('\t', ctypes.string_at(id(result), sys.getsizeof(result)))
# print('\t', struct.unpack('LLLLli' + 'c' *  6, ctypes.string_at(id(result), sys.getsizeof(result))))

# Введите число = 12345
#  id= 5073088, type= <class 'str'>, size= 30, object= 12345
# 	 b'\x01\x00\x00\x000nF\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x00\x00\x00\x00\x00\x00\x0012345\x00'
# 	 (1, 1548119600, 5, 4294967295, 228, 0, b'1', b'2', b'3', b'4', b'5', b'\x00')
#  id= 1776352, type= <class 'str'>, size= 25, object=
# 	 b'<\x00\x00\x000nF\\\x00\x00\x00\x00\x00\x00\x00\x00\xe5\x00\x00\x00\x00\x00\x00\x00\x00'
# 	 (60, 1548119600, 0, 0, 229, 0, b'\x00')
# Обратное число =  54321
#  id= 5073088, type= <class 'str'>, size= 30, object= 12345
# 	 b'\x01\x00\x00\x000nF\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x00\x00\x00\x00\x00\x00\x0012345\x00'
# 	 (1, 1548119600, 5, 4294967295, 228, 0, b'1', b'2', b'3', b'4', b'5', b'\x00')
#  id= 5113184, type= <class 'str'>, size= 30, object= 54321
# 	 b'\x01\x00\x00\x000nF\\\x05\x00\x00\x00\xff\xff\xff\xff\xe4\x00\x00\x00\x00\x00\x00\x0054321\x00'
# 	 (1, 1548119600, 5, 4294967295, 228, 0, b'5', b'4', b'3', b'2', b'1', b'\x00')



# Выводы и наблюдения
# вариант решения через числовые операции занимает меньше места чем через строку
# для большого числа (проверял на 34 разряда) строка занимает больше места 
