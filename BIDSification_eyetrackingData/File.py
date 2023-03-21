#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import csv

def open_file(filename, filepath):

    '''
    Open the files json, tsv or asc

    Parameters
    ----------
    filename: str
        Name of the file
    filepath: str
        Path of the file

    Returns
    -------
    file
        list, dict, list of dict or None
    '''

    # file format
    fileformat = filename.split('.')[-1]

    if fileformat in ['json', 'tsv', 'asc']:

        if filepath:
            filename = os.path.join(filepath, filename)

        f = open(filename, 'r')

        # open file .json
        if fileformat=='json':
            file_ = json.load(f)

        # open file .tsv
        elif fileformat=='tsv':
            from copy import copy
            file_ = copy(list(csv.DictReader(f, delimiter=" ")))

        # open file .asc
        elif fileformat=='asc':
            file_ = f.readlines()

        f.close()

        return file_

    else:
        return None

def save_file(data, filename, filepath):

    '''
    Save the data in files json or tsv

    Parameters
    ----------
    data: list or dict
        Data to be saved
    filename: str
        Name of the file
    filepath: str (default None)
        Path of the file
    '''

    # file format
    fileformat = filename.split('.')[-1]

    if fileformat in ['json', 'tsv']:

        filename = os.path.join(filepath, filename)
        f = open(filename, 'w')

        # save file .json
        if fileformat=='json':
            json.dump(data, f, indent=4)

        # save file .tsv
        elif fileformat=='tsv':
            file_ = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=' ')
            file_.writeheader()
            file_.writerows(data)

        f.close()

