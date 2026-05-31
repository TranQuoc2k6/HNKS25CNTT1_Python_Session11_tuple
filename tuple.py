
"""
    - TUPLE: là 1 kiểu dữ liệu, dùng để lưu trữ kiểu dữ liệu dạng danh sách nhưng danh sánh đó không thể thao tác (thêm , sửa, xóa)
    - Ứng dụng: lưu tọa độ, lưu các hằng số toán học, các danh sách cố định(danh sách các thứ trong tuần, các tháng trong năm, ...)
    - Cách khai báo: 
        my_touple = ("tháng 1", "tháng 2") 
        print(my_tuple[1])
    - Khi khai báo tuple có 1 phần tử bắt buộc phải có dấu phẩy ở cuối
"""

# Các cách để tạo 1 tuple
# Cách 1:
my_tuple = (1, 2, 3, 4)
print(f"my_tuple: {my_tuple}")

# Cách 2:
my_tuple_packing = 1, 2, 3, 4
print(f"my_tuple_packing: {my_tuple_packing}")

# Khi khai báo tuple có 1 phần tử duy nhất
my_single_tuple = (1,) 
print(f"my_single_tuple: {my_single_tuple}")

# Bảo vệ dữ liệu
toa_do = (10, 20)

toa_do[0] = 50 

