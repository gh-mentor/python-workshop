import unittest
from queue import Queue
from src.producer import Producer
from src.consumer import Consumer

class TestConsumer(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.consumer = Consumer(self.queue)

    def test_consume(self):
        # Arrange
        self.queue.put("item1")
        self.queue.put("item2")

        # Act
        item1 = self.consumer.consume()
        item2 = self.consumer.consume()

        # Assert
        self.assertEqual(item1, "item1")
        self.assertEqual(item2, "item2")

    def test_consume_empty_queue(self):
        # Act
        item = self.consumer.consume()

        # Assert
        self.assertIsNone(item)

if __name__ == "__main__":
    unittest.main()