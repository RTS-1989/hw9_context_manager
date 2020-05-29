from datetime import datetime
from time import sleep
from cook_book_v2 import get_shop_list_by_dishes
from cook_book_v2 import file_to_cb


class Codetimecounter:

    def __init__(self, log_path, encoding='utf8'):
        self.log_file = open(log_path, 'a', encoding=encoding)
        self.name = self.__class__.__name__

    def __enter__(self):
        self.start = datetime.now()
        self.log_file.write(f'Старт функции {self.name}: {self.start}: \n')
        return self

    def write_trace_log(self, function):
        self.function = function
##        self.function('recipes.txt')
        self.function(['Омлет', 'Фахитос'], 2)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_trace_log(f'error: {exc_val}')
        self.end = datetime.now()
        self.log_file.write(f'Конец функции {self.name}: {self.end}" \n')
        self.runtime = self.end - self.start
        self.log_file.write(f'Время работы функции {self.name}: {self.runtime}: \n')
        self.log_file.close()
        print(f'Старт функции {self.name}: {self.start}: \n\
Конец функции {self.name}: {self.end} \n\
Время выполнения функции {self.name} составляет: {self.runtime}'
              )

if __name__ == '__main__':
    with Codetimecounter('my.log') as log:
##        log.write_trace_log(file_to_cb)
        log.write_trace_log(get_shop_list_by_dishes)