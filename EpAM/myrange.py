class Myrange:

    def __init__(self, start, stop=None, step=1):
        self.type_check(start)
        if stop is None:
            self.__start = 0
            self.__stop = start
        else:
            self.__start = start
            self.type_check(stop)
            self.__stop = stop
        self.type_check(step, flag_step=True)
        self.__step = step
        self.__result_list = Myrange._result_list(self.__start,
                                                  self.__stop,
                                                  self.__step)

    @staticmethod
    def _result_list(start, stop, step=1):
        __list_items = []
        if step < 0:
            res = start
            while stop < res and start > stop:
                __list_items.append(res)
                res += step
        else:
            res = start
            while stop > res and start < stop:
                __list_items.append(res)
                res += step
        return __list_items

    def index(self, value):
        try:
            return self.__result_list.index(value)
        except ValueError:
            return f"ValueError: {value} is not in range"

    def count(self, value):
        try:
            return self.__result_list.count(value)
        except ValueError:
            return f"ValueError: {value} is not in range"

    def __iter__(self):
        res = self.__start
        if self.__step < 0:
            while self.__stop < res and self.__start > self.__stop:
                yield res
                res += self.__step
            return
        else:
            while self.__stop > res and self.__start < self.__stop:
                yield res
                res += self.__step
            return

    def __getitem__(self, item):
        if isinstance(item, int):
            try:
                return self.__result_list[item]
            except IndexError:
                raise IndexError(f"range object index out of range")

        if isinstance(item, slice) and self.__result_list:
            start, stop = get_index_of_range(self.__step, item.start, item.stop, self.__result_list)
            step = get_index_by_step(self.__step, item.step)

        elif not self.__result_list:
            start = self.__start
            stop = self.__start
            if item.step != None:
                step = item.step * self.__step
            else:
                step = self.__step

        return Myrange(start, stop, step)

    def __str__(self):
        if self.__step == 1:
            return f'range({self.__start},{self.__stop})'
        else:
            return f'range({self.__start},{self.__stop},{self.__step})'

    def type_check(self, value, flag_step=None):
        if not isinstance(value, int):
            raise TypeError('Value must be int')
        if flag_step != None and value == 0:
            raise ValueError("Step value does't be 0")

    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop

    @property
    def step(self):
        return self.__step


def get_index_of_range(base_step: int, start: int = None, stop: int = None, list_of_items: list = None):
    '''
    Функция вычисляет начальное и конечное значения для заданной последовательности,
    с текушим шагом, по индексам start и stop.
    :param base_step: текущий шаг последовательности, тип int
    :param start: - начальный индекс среза, тип int
    :param stop: - конечный индекс среза, тип int
    :param list_of_items: - исходная последовательность
    :return: возвращает итоговые начальные и конечные значения
    '''
    if start != None:
        if start < 0:
            if start <= -len(list_of_items):
                start = list_of_items[0]
            else:
                start = list_of_items[start]
        elif start > 0:
            if start >= len(list_of_items):
                start = list_of_items[-1] + base_step
    else:
        start = list_of_items[0]
    if stop != None:
        if stop < 0:
            if stop <= -len(list_of_items):
                stop = list_of_items[0]
        elif stop > 0:
            if stop >= len(list_of_items):
                stop = list_of_items[-1] + base_step
        else:
            stop = list_of_items[-1]
    else:
        stop = list_of_items[-1]
    return start, stop


def get_index_by_step(base_step: int, step=None):
    if step != None:
        step = step * base_step
    else:
        step = base_step
    return step


