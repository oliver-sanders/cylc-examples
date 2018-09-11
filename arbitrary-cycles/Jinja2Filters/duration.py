"""Custom Jinja2 filter module for computing ISO8601 durations in cylc."""

import os
from pipes import quote
from subprocess import Popen, PIPE


def duration(date_a, date_b):
    """Return the duration between two ISO8601 dates.

    Basic wrapper for the `rose date` command.

    Examples:
        >>> duration('2000', '2001')
        'P366D'
        >>> duration ('2001-01-01T00', '2000-12-31T12')
        '-PT12H'

    """
    command = ['rose', 'date', quote(date_a), quote(date_b)]
    proc = Popen(
        command,
        stdin=open(os.devnull),
        stdout=PIPE,
        stderr=PIPE)
    if proc.wait():
        raise Exception(proc.communicate()[1])
    return proc.communicate()[0].strip()
