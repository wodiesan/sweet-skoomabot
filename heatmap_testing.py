"""
Test file for generating plot.ly heatmp data.
Example heatmap can be found here:
https://plot.ly/~wodiesan/56/test-heatmap-of-poly-drug-posts/

coord_to_matrix function needs work.
"""
# import druggiebot_config as dbc

# mainviz_xaxis = dbc.plotly_dict.keys()
# print mainviz_xaxis
# print len(mainviz_xaxis)

# Hard coding mainviz_xaxis to allow for testing without importing files.
mainviz_xaxis = ['lsd', 'nicotine', 'painkiller', 'otc', 'ecstasy', 'heroin', 'psilocybin', 'meth', 'cocaine', 'amphetamine', 'alcohol', 'benzo', 'caffeine', 'cannabis', 'salvia']
print mainviz_xaxis

heat_matrix = [[0 for x in range(len(mainviz_xaxis))] for x in range(len(mainviz_xaxis))]
print heat_matrix

# TEST DATASETS FROM ACTUAL TITLE RESULTS
result = ['nicotine', 'lsd']
result2 = ['nicotine', 'lsd', 'ecstasy']
result3 = ['ecstasy', 'lsd', 'cannabis', 'cocaine']


def parse_poly(poly_list):
    """Finds the index for each drug in the list."""
    coord_list = []
    for item in poly_list:
        coord_index = mainviz_xaxis.index(item)
        coord_list.append(coord_index)

    print '\nYour indices for {}: {}'.format(poly_list, coord_list)
    return coord_list


# def coord_recursion(coord_list, index):
#     """Ensures that each list index is checked against the entire range."""
#     recursion_amt = len(coord_list)
#     x = 0
#     while x < recursion_amt:
#         try:
#             index_increment = coord_list.index(index)
#             position = [index, coord_list[index_increment]]
#         except IndexError:
#             pass
#         # coord_recursion(coord_list, coord_list.index(index + 1))
#         x += 1
#     return position


def coord_to_matrix(coord_list):
    """Takes a list of indicies, returns position in the heatmap matrix.

    HERE BE TROUBLE. 
    I'm looking for something like [[1, 0],[1, 4],[0, 4]]
    for the result2 dataset. It should be easy, but my brain is fried right now."""
    heatmap_coord_list = []
    for item in coord_list:
        for x in range(len(coord_list)):
            try:
            # while x > len(coord_list):
            #     index = coord_list.index(item)
            #     position = [item, coord_list[index + 1]]
            #     print 'pos: {}'.format(position)
            #     heatmap_coord_list.append(position)
            #     x += 1
            # for x in range(len(coord_list)):
                # index_increment = coord_list.index(item) # 15JUN JUST COMMENTED OUT
                index_increment = coord_list.index(item += 1)
                position = [item, coord_list[index_increment]]
                # position = coord_recursion(coord_list, index_increment)
                heatmap_coord_list.append(position)
            except IndexError:
                pass

    print '\nYour pos for {}:'.format(heatmap_coord_list)
    return heatmap_coord_list

get_indices = parse_poly(result2)
get_pos = coord_to_matrix(get_indices)

# for coordinates in range(len(result2)):
#     print  += 1
# for item in result:
#     print mainviz_xaxis.index(item)
