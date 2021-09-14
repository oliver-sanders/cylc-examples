from isodatetime.data import Duration, TimePoint
from isodatetime.parsers import TimeRecurrenceParser, TimePointParser, DurationParser


def duration_to_time(duration, offset='00'):
    """Convert a duration to list of times of the day.

    Works with durations that are shorter than one day.

    Arguments:
        duration (str):
            The duration as a string e.g. "PT3H".
        offset (str):
            The offset from which to count,
            (i.e. the earliest time to consider).
            e.g. "00" (midnight, the default)

    Examples:
        # every six hours starting at T00
        >>> list(duration_to_time('PT6H'))
        ['T0000', 'T0600', 'T1200', 'T1800']
        
        # every six hours starting at T0030
        >>> list(duration_to_time('PT6H', '0030'))
        ['T0030', 'T0630', 'T1230', 'T1830']
    """
    tp1 = TimePointParser().parse('20000101T' + offset + 'Z')
    tp2 = TimePointParser().parse('20000102T00Z')
    dur = DurationParser().parse(duration)
    while tp1 < tp2:
        yield 'T%02d%02d' % (tp1.hour_of_day, tp1.minute_of_hour)
        tp1 = tp1 + dur

