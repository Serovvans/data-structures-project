import pytest

from src.queue import Queue

@pytest.fixture(scope="session")
def queue():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    return queue
