import logging

import pytest

from subregistry import add_registry


def test_add_registry():

    @add_registry
    class Test:
        pass

    assert hasattr(Test, "registry")
    assert Test.registry.registry == tuple()


def test_add_registry_custom_name():

    @add_registry(registry_name="custom")
    class Test:
        pass

    assert hasattr(Test, "custom")
    assert Test.custom.registry == tuple()


def test_add_registry_include_base():

    @add_registry(exclude_base=False)
    class Test:
        pass

    assert hasattr(Test, "registry")
    assert Test.registry.registry == (Test,)


def test_warn_init_subclass(caplog):

    with caplog.at_level(logging.WARNING):
        @add_registry
        class Test:
            def __init_subclass__(cls):
                pass  # Warn me!

        assert "already defines '__init_subclass__()'" in caplog.text


def test_registry_name_error():

    with pytest.raises(ValueError):
        @add_registry
        class Test:
            registry = object()
