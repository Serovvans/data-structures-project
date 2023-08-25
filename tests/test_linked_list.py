"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList


def test_linked_list():
    ll = LinkedList()

    # Добавляем данные
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})

    # Печатаем данные
    assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"


def test_to_list(ll):
    lst = ll.to_list()
    assert lst[0] == {'id': 0, 'username': 'serebro'}
    assert lst[1] == {'id': 1, 'username': 'lazzy508509'}
    assert lst[2] == {'id': 2, 'username': 'mik.roz'}
    assert lst[3] == {'id': 3, 'username': 'mosh_s'}


def test_by_id(ll):
    user_data = ll.get_data_by_id(3)
    assert user_data == {'id': 3, 'username': 'mosh_s'}
