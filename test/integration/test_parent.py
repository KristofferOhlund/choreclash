import pytest
from choreclash.models.parent import Parent
from choreclash.models.children import Child

def test_parent_children_relationship():
    # Arrange
    # Create a Parent instance
    parent = Parent(first_name="John", last_name="Doe", email="john.doe@example.com")
    # Create Child instances
    child1 = Child(first_name="Alice", parent_id=parent.id)
    child2 = Child(first_name="Bob", parent_id=parent.id)

    # Act
    # Add children to parent
    parent.children.append(child1)
    parent.children.append(child2)

    # Assert the relationship
    assert len(parent.children) == 2
    assert parent.children[0].first_name == "Alice"
    assert parent.children[1].first_name == "Bob"