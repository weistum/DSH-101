# TODO Найдите количество книг, которое можно разместить на дискете

string = 25  # Количество символов в строке
page = 50  # Количество строк в странице
book = 100  # Количество страниц в книге
disk = 1.44  # Объем дискеты
simbol_size = 4  # Количество байт информации которые занимает один символ

simbols_in_book = string * page * book  # Расчет количества символов в вниге
book_size = simbols_in_book * simbol_size  # Расчет места на диске (байт) необходимого для размещения одной книги

bytes_on_disk = disk * 1024 * 1024  # Расчет объема дискеты в байтах

total_books = round(bytes_on_disk // book_size)

print("Количество книг, помещающихся на дискету:", total_books)
