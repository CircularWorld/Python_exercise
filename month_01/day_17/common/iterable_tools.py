class IterableHelper:
    @staticmethod
    def find_all(iterable, func):

        for item in iterable:
            if func(item):
                yield item
    @staticmethod
    def select(iteratror, func):
        for item in iteratror:
            yield func(item)

    @staticmethod
    def find_single(iteratror, func):
        for item in iteratror:
            if func(item):
                return item

