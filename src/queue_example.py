class Queue(object):
    """Queue class with push and pop methods"""

    def __init__(self):
        """Queue constructor"""
        self.stack_enqueue = []
        self.stack_dequeue = []

    def __str__(self):
        """String representation of Queue objects"""
        return (f'Elements_to_queue {self.stack_enqueue}\n'
                f'Elements_in_queue {self.stack_dequeue}')

    def queue_is_empty(self):
        """Check if any elements are in queue"""
        return len(self.stack_dequeue) == 0

    def to_queue_is_empty(self):
        """Check if any elements are to queue"""
        return len(self.stack_enqueue) == 0

    def push(self, element):
        """Add element to queue

        :param element: Object for queue
        :return: None
        """
        self.stack_enqueue.append(element)

    def pop(self):
        """Remove first element from queue and return it

        :return: Element that first in Queue
        """
        if self.queue_is_empty():
            if self.to_queue_is_empty():
                print('Queue is empty')
                return

            while not self.to_queue_is_empty():
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()
