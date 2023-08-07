class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            self.tail = Node(data, None)
            self.head = self.tail
        else:
            new = Node(data, None)
            self.tail.next_node = new
            self.tail = new


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is not None:
            data = [self.head.data]
            curr = self.head
            while curr.next_node is not None:
                curr = curr.next_node
                data.append(curr.data)
        else:
            data = []
        return "\n".join(data)
