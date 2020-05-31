import pandas as pd
import collections
from ordered_set import OrderedSet
import copy


def dfs_list(itemsets, frequentSet):
    # Depth first search frequent itemset mining algorithm
    itemsets = remove_infrequent_items(itemsets, threshold)
    print("Database %s and itemsets" % itemsets, frequentSet)
    linear_order = list(OrderedSet(sum(itemsets, [])))
    for parsing in linear_order:
        itemsets1 = copy.deepcopy(itemsets)
        itemsets1 = sort_items_order(itemsets1, parsing)
        frequentSet = frequentSet + parsing
        items = 0
        while items < len(itemsets1):
            if parsing in itemsets1[items]:
                itemsets1[items].remove(parsing)
                items = items + 1
            else:
                itemsets1.remove(itemsets1[items])
        dfs_list(copy.deepcopy(itemsets1), frequentSet)
        frequentSet = frequentSet[:-1]
    return frequentSet


def sort_items_order(itemset, frequentSet):
    # Deleting the items according to the defined linear order
    if frequentSet:
        if frequentSet[-1] in numItems:
            i = numItems.index(frequentSet[-1])
            for i in numItems[:i]:
                k = 0
                while k < len(itemset):
                    if i in itemset[k]:
                        itemset[k].remove(i)
                    else:
                        k = k + 1
    return itemset


def remove_infrequent_items(itemsets, t):
    # Delete all the infrequent items
    probemap = collections.OrderedDict()
    tmp = sum(itemsets, [])
    n = len(itemsets)
    for i in tmp:
        probemap[i] = tmp.count(i)
    for i in range(n):
        k = 0
        while k < len(itemsets[i]):
            if probemap[itemsets[i][k]] < t:
                itemsets[i].remove(itemsets[i][k])
            else:
                k = k + 1
    return itemsets


def find_order(itemsets):
    # Selects an linear order
    tmp = list(OrderedSet(sum(itemsets, [])))
    if tmp:
        for i in range(len(linear_order)):
            if linear_order[i] in tmp:
                return linear_order[i:]
    return [0]


data = {'TID': [1,2,3,4,5], 'Itemset': [list('MONKEY'), list('DONKEY'), list('MAKE'), list('MUCKY'), list('COKE')]}
# data = {'TID': [1,2,3], 'Itemset': [list('abd'), list('abcd'), list('cd')]}
df = pd.DataFrame(data)

database = df['Itemset'].tolist()

linear_order = list(OrderedSet(sum(database, [])))

threshold = 2
frequentItemset = []

numItems = list(OrderedSet(sum(database, [])))

dfs_list(copy.deepcopy(database), "")
