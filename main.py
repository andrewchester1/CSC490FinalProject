class Bin(object):
    def __init__(self):
        self.items = []
        self.sum = 0

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def __str__(self):
        return 'Bin(sum=%d, items=%s)' % (self.sum, str(self.items))


def pack(values, maxValue):
    values = sorted(values, reverse=True)
    bins = []

    for item in values:
        for bin in bins:
            if bin.sum + item <= maxValue:
                bin.append(item)
                break
        else:
            print('Making new bin for', item)
            bin = Bin()
            bin.append(item)
            bins.append(bin)

    return bins


if __name__ == '__main__':
    import random

    def packAndShow(aList, maxValue):
        print('List with sum', sum(aList), 'requires at least', (sum(aList)+maxValue-1)/maxValue, 'bins')

        bins = pack(aList, maxValue)

        print('Solution using', len(bins), 'bins:')
        for bin in bins:
            print(bin)

        print


    aList = [10,9,8,7,6,5,4,3,2,1]
    packAndShow(aList, 11)

    aList = [ random.randint(1, 11) for i in range(100) ]
    packAndShow(aList, 11)
