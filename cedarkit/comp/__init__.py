from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("cedarkit.comp")
except PackageNotFoundError:
    # package is not installed
    pass
