import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse('abc'))
print(my_utils.str_util.substr('abc', 0, 1))

file_util.print_file_info("E:/面试技术/bill.txt")
file_util.append_to_file("E:/面试技术/bill.txt", "111")