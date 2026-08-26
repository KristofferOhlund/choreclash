from pytest import fixture

@fixture
def parent():
    from choreclash.models.parent import Parent
    return Parent(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com"
    )

def test_parent_children_relationship(parent):
    from choreclash.models.children import Child
    child1 = Child(first_name="Alice", parent_id=parent.id)
    child2 = Child(first_name="Bob", parent_id=parent.id)
    
    parent.children.append(child1)
    parent.children.append(child2)
    
    assert len(parent.children) == 2
    assert parent.children[0].first_name == "Alice"
    assert parent.children[1].first_name == "Bob"

    