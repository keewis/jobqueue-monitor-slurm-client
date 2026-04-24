from importlib.metadata import version

try:
    __version__ = version("slurm_client")
except Exception:
    __version__ = "9999"
