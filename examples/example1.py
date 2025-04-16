"""Basic example showing how to use the `add_registry` decorator."""


from subregistry import add_registry


@add_registry
class BaseClass:
    pass


class ChildA(BaseClass):
    pass


class ChildB(BaseClass):
    pass


class ChildC(ChildB):
    pass


if __name__ == "__main__":
    print("Running example.")
    print("Classes in registry:", BaseClass.registry.registry)

    ClassA = BaseClass.registry.get_by_name("ChildA")
    instance_a = ClassA()
    print("Is correct class:", isinstance(instance_a, ChildA))
