import pytest
from contacts_tree import ContactsTree
from node import Node

MOCK_CONTACTS = [
    ("Alice Smith", "alice.smith@email.com"),
    ("Bob Johnson", "bob.j@email.com"),
    ("Carol Wilson", "carol.w@email.com"),
    ("David Thompson", "david.t@email.com"),
    ("Amy Brown", "amy.brown@email.com"),
]

@pytest.fixture
def empty_tree():
    """Provide an empty ContactsTree instance for testing."""
    return ContactsTree()


@pytest.fixture
def populated_tree():
    """Provide a ContactsTree pre-populated with test data."""
    tree = ContactsTree()
    for name, email in MOCK_CONTACTS:
        tree.insert(name, email)
    return tree


@pytest.fixture
def contacts_tree():
    """Provide a ContactsTree instance for testing."""
    return ContactsTree()


def test_node_creation():
    """Test that Node objects are created with correct attributes."""
    node = Node("John Doe", "john@email.com")
    assert node.name == "John Doe"
    assert node.email == "john@email.com"
    assert node.left is None
    assert node.right is None


class TestNodeProperties:
    """Test Node class properties for name extraction."""
    
    def test_node_first_name_property(self):
        """Test extraction of first names using Node property."""
        node1 = Node("John Doe", "john@email.com")
        node2 = Node("Mary Jane Watson", "mary@email.com")
        node3 = Node("Cher", "cher@email.com")
        
        assert node1.first_name == "John"
        assert node2.first_name == "Mary"
        assert node3.first_name == "Cher"
    
    def test_node_last_name_property(self):
        """Test extraction of last names using Node property."""
        node1 = Node("John Doe", "john@email.com")
        node2 = Node("Mary Jane Watson", "mary@email.com")
        node3 = Node("Cher", "cher@email.com")
        
        assert node1.last_name == "Doe"
        assert node2.last_name == "Watson"
        assert node3.last_name == "Cher"


class TestInsertion:
    """Test contact insertion functionality."""
    
    def test_insert_single_contact(self, empty_tree):
        """Test inserting a single contact into an empty tree."""
        empty_tree.insert("John Doe", "john@email.com")
        assert empty_tree.root is not None
        assert empty_tree.root.name == "John Doe"
        assert empty_tree.root.email == "john@email.com"
    
    def test_insert_multiple_contacts_tree_not_empty(self, empty_tree):
        """Test that inserting multiple contacts creates a non-empty tree."""
        for name, email in MOCK_CONTACTS:
            empty_tree.insert(name, email)
        
        assert empty_tree.root is not None
    
    def test_insert_multiple_contacts_all_present(self, empty_tree):
        """Test that all inserted contacts can be found in the tree."""
        for name, email in MOCK_CONTACTS:
            empty_tree.insert(name, email)
        
        # Verify all contacts can be found
        for name, email in MOCK_CONTACTS:
            found = empty_tree.search(name)
            assert found is not None
            assert found.name == name
            assert found.email == email
    
    def test_insert_multiple_contacts_sorted_by_last_name(self, empty_tree):
        """Test that multiple contacts are sorted by last name."""
        for name, email in MOCK_CONTACTS:
            empty_tree.insert(name, email)
        
        sorted_contacts = empty_tree.inorder_traversal()
        last_names = [contact.last_name for contact in sorted_contacts]
        
        assert last_names == sorted(last_names)
    
    def test_insert_multiple_contacts_traversal_length(self, empty_tree):
        """Test that traversal returns the correct number of contacts."""
        for name, email in MOCK_CONTACTS:
            empty_tree.insert(name, email)
        
        sorted_contacts = empty_tree.inorder_traversal()
        assert len(sorted_contacts) == len(MOCK_CONTACTS)


class TestSearch:
    """Test contact search functionality."""

    def test_search_existing_contact(self, populated_tree):
        """Test searching for an existing contact."""
        found = populated_tree.search("Alice Smith")
        assert found is not None
        assert found.name == "Alice Smith"
        assert found.email == "alice.smith@email.com"
    
    def test_search_nonexistent_contact(self, populated_tree):
        """Test searching for a non-existent contact returns None."""
        found = populated_tree.search("Nobody Here")
        assert found is None


class TestTraversal:
    """Test tree traversal functionality."""
    
    def test_inorder_traversal_empty_tree(self, empty_tree):
        """Test that traversal of empty tree returns empty list."""
        result = empty_tree.inorder_traversal()
        assert result == []
    
    def test_inorder_traversal_sorted_order(self, populated_tree):
        """Test that traversal returns contacts in sorted order."""
        sorted_contacts = populated_tree.inorder_traversal()
        
        # Extract last names to verify sorting using Node property
        last_names = [contact.last_name for contact in sorted_contacts]
        
        # Should be in alphabetical order by last name
        assert last_names == sorted(last_names)
        
        # Verify all contacts are present
        assert len(sorted_contacts) == len(MOCK_CONTACTS)