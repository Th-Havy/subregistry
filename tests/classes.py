from subregistry import add_registry


@add_registry
class Base:
    pass


class A(Base):
    pass


class B(Base):
    pass


class C(B):
    pass
