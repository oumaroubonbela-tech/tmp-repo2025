# TODO Найдите количество книг, которое можно разместить на дискете
disk_space = 1.44
book_pages = 100
line_pages = 50
line_character = 25
space_per_character = 4
book_lines = book_pages * line_pages
book_character = book_lines * line_character
book_space = book_character * space_per_character
book_space_in_kb = book_space / 1024
book_space_in_mb = book_space_in_kb / 1024
number_of_book = int(1.44/book_space_in_mb)
# print("number lines in one book is:", book_lines )
# print("number lines in one book is:", book_character )
# print("number lines in one book is:", book_space )
# print("space of one book :", book_space_in_mb )
# print("number of book:", number_of_book )
print("Количество книг, помещающихся на дискету:", number_of_book)
