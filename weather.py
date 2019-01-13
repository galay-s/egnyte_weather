# coding=utf-8
import pandas as pd
from settings import FILE_NAME, FWIDTHS, INDEX_COL


def remove_asterisk(val):
    """Removes asterisk.
    Some rows have '*' at the end of value 'MxT' or 'MnT'.
    """
    new_val = val.replace('*', '')
    return float(new_val)


def get_day(df):
    """Returns the day number (column one) with the smallest temperature spread."""
    return (df['MxT'] - df['MnT']).abs().idxmin()


if __name__ == '__main__':
    df = pd.read_fwf(
        FILE_NAME,
        widths=FWIDTHS,
        converters={'MxT': remove_asterisk, 'MnT': remove_asterisk},
        skipfooter=1,
        skiprows=[1],
        index_col=INDEX_COL
    )
    print "Day with the smallest temperature spread is {}".format(get_day(df))
