"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

Config file that contains the various:
1. Dictionaries and lists of terms.
2. Functions to build dicts and lists for charting in plot.ly.
"""

from collections import OrderedDict


def create_matrix(dict_category):
    """Takes a dict and returns matrix with x and y at dict legnth."""
    matrix_vals = dict_category
    matrix = [[0 for x in range(len(matrix_vals))]
              for x in range(len(matrix_vals))]
    return matrix


def create_matrix_2cats(dict_x_cat, dict_y_cat):
    """Takes a dict and returns matrix with x and y at dict legnth."""
    matrix_x_vals = dict_x_cat
    matrix_y_vals = dict_y_cat
    matrix = [[0 for x in range(len(matrix_x_vals))]
              for x in range(len(matrix_y_vals))]
    return matrix


def dict_wo_vals(dict_w_vals):
    """Takes a dict, returns new dict with None vals for all keys."""
    copy_dict = OrderedDict.fromkeys(dict_w_vals.keys(), None)
    return copy_dict


def sub_dict_wo_vals(list_of_subcategories):
    """Creates a dict with the list items as key and None as vals."""
    sub_dict = OrderedDict()
    for item in list_of_subcategories:
        sub_dict[item] = None
    return sub_dict


def init_axes(category_dict):
    """Initializes lists and dictionaries to be used by plot.ly."""
    py_dict = dict_wo_vals(category_dict)
    py_list = py_dict.keys()
    py_matrix = create_matrix(category_dict)
    return py_dict, py_list, py_matrix


def init_subcategory(list_of_subcategories):
    """Takes in a dict's key that contains a list of subcategories to match."""
    subcat_dict = sub_dict_wo_vals(list_of_subcategories)
    subcat_list = subcat_dict.keys()
    return subcat_dict, subcat_list


# def init_subcategories(category_dict):
#     """Takes a dict of categories and returns a dict and list for 
#     each key's val, which are all lists."""
#     for key in category_dict.keys():
#         sub_dict, sub_list = init_subcategory(key)
