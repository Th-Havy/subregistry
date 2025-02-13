import logging
from importlib import util
from pathlib import Path


logger = logging.getLogger(__file__)


class SubclassRegistry:

    def __init__(self):
        self._registry = []

    @property
    def registry(self) -> tuple[type]:
        return tuple(self._registry)

    def get_by_name(self, name: str) -> type:
        """Returns a model class from the registry given its name."""

        for klass in self.registry:
            if klass.__name__ == name:
                return klass

        raise ValueError(f"Model '{name}' not found in registry.")

    def load_subclasses(self, module_path: Path, recursive: bool = False):
        """Load one or more modules such that its subclasses are registered.

        Args:
            module_path: Path of the module to dynamically load. It can be a single `.py` file, or a folder containing
                multiple python files.
            recursive: if `module_path` is a folder, all its subfolders will also be dynamically loaded.
        """

        # Single modules
        if module_path.is_file():
            if module_path.suffix != ".py":
                raise ValueError(f"File '{module_path}' is not a Python module.")
            self._load_module(module_path)
            return

        # TODO: Case module
        # TODO: Case recursive

    @staticmethod
    def _load_module(path: Path):
        """Automatically load a module."""

        logger.debug("Loading module:", path)
        name = path.name
        spec = util.spec_from_file_location(name, path)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module