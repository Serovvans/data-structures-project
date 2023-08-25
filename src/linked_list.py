class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        self.tail = None
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, self.tail)
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data, None)
        if self.tail is None:
            self.head.next_node = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()

    def to_list(self) -> list:
        lst = []
        curr = self.head
        while curr is not None:
            lst.append(curr.data)
            curr = curr.next_node

        return lst

    def get_data_by_id(self, item_id: int) -> dict:
        curr = self.head
        while self.head is not None:
            try:
                if curr.data["id"] == item_id:
                    return curr.data
            except KeyError:
                print("В словаре нет id")
            except TypeError:
                print("Данные не являются словарем")

            curr = curr.next_node
