# -*- coding: utf-8 -*-
"""Stable configuration keys in ascending graphic-equalizer frequency order."""

# The original 16 kHz band keeps key 8. Key 9 adds 12 kHz without moving
# values in existing NVDA configurations or configuration profiles.
GRAPHIC_EQ_KEYS = tuple("graphic_eq_%d" % index for index in (0, 1, 2, 3, 4, 5, 6, 7, 9, 8))


def get_graphic_eq_gains(section):
    """Read ten gains; an absent new 12 kHz setting defaults to zero."""
    return [section.get(key, 0) for key in GRAPHIC_EQ_KEYS]
