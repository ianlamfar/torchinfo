from __future__ import annotations

from enum import Enum, IntEnum, unique, StrEnum


@unique
class Mode(StrEnum):
    """Enum containing all model modes."""

    __slots__ = ()

    TRAIN = "train"
    EVAL = "eval"


@unique
class RowSettings(StrEnum):
    """Enum containing all available row settings."""

    __slots__ = ()

    DEPTH = "depth"
    VAR_NAMES = "var_names"
    ASCII_ONLY = "ascii_only"
    HIDE_RECURSIVE_LAYERS = "hide_recursive_layers"


@unique
class ColumnSettings(StrEnum):
    """Enum containing all available column settings."""

    __slots__ = ()

    KERNEL_SIZE = "kernel_size"
    INPUT_SIZE = "input_size"
    OUTPUT_SIZE = "output_size"
    NUM_PARAMS = "num_params"
    PARAMS_PERCENT = "params_percent"
    MULT_ADDS = "mult_adds"
    MULT_ADDS_PERCENT = "mult_adds_percent"
    TRAINABLE = "trainable"


@unique
class Units(StrEnum):
    """Enum containing all available bytes units."""

    __slots__ = ()

    AUTO = "auto"
    BYTES = "B"
    KILOBYTES = "KB"
    MEGABYTES = "MB"
    GIGABYTES = "GB"
    TERABYTES = "TB"
    KILO = "K"
    MEGA = "M"
    GIGA = "G"
    TERA = "T"
    NONE = ""


@unique
class Verbosity(IntEnum):
    """Contains verbosity levels."""

    QUIET, DEFAULT, VERBOSE = 0, 1, 2
