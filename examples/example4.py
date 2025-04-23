"""Example demonstrating how to change the registry name and how to include the base class in the registry."""


from subregistry import add_registry


@add_registry(registry_name="other_registry", exclude_base=False)
class BaseClass:
    registry = "Attribute named 'registry' already used"


class Subclass(BaseClass):
    pass


if __name__ == "__main__":
    print("Running example.")
    print("Classes in registry:", BaseClass.other_registry.registry)
    assert BaseClass == BaseClass.other_registry.get_by_name("BaseClass")
