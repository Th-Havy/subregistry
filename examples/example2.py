"""Example demonstrating how the registry works when importing modules that contain subclasses."""


from .base import BaseClass
from . import child


if __name__ == "__main__":
    print("Running example.")
    print("Classes in registry:", BaseClass.registry.registry)
