import unittest
from models import storage
from models.state import State
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Tear down test environment."""
        self.storage.delete(self.state)

    def test_get(self):
        """Test the get method."""
        state_id = self.state.id
        self.assertIs(self.storage.get(State, state_id), self.state)
        self.assertIsNone(self.storage.get(State, "non_existent_id"))

    def test_count(self):
        """Test the count method."""
        initial_count = self.storage.count(State)
        new_state = State(name="Texas")
        new_state.save()
        self.assertEqual(self.storage.count(State), initial_count + 1)
        self.assertEqual(self.storage.count(), initial_count + 1)

if __name__ == "__main__":
    unittest.main()
