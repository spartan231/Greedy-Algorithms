# FIFO (First In First Out)
def fifo(pages, capacity):
    page_set = set()
    page_queue = []
    page_faults = 0

    for page in pages:
        if page not in page_set:
            if len(page_set) < capacity:
                page_set.add(page)
                page_queue.append(page)
            else:
                oldest_page = page_queue.pop(0)
                page_set.remove(oldest_page)
                page_set.add(page)
                page_queue.append(page)
            page_faults += 1

    return page_faults

# LRU (Least Recently Used)
def lru(pages, capacity):
    page_set = set()
    page_queue = []
    page_faults = 0

    for page in pages:
        if page not in page_set:
            if len(page_set) < capacity:
                page_set.add(page)
                page_queue.append(page)
            else:
                least_recently_used_page = page_queue.pop(0)
                page_set.remove(least_recently_used_page)
                page_set.add(page)
                page_queue.append(page)
            page_faults += 1
        else:
            # Move the accessed page to the end of the queue
            page_queue.remove(page)
            page_queue.append(page)

    return page_faults

# OPTFF (Belady’s Farthest-in-Future, optimal offline)
def optff(pages, capacity):
    page_set = set()
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page not in page_set:
            if len(page_set) < capacity:
                page_set.add(page)
            else:
                # Find the page that will not be used for the longest time
                farthest_page = None
                farthest_index = -1
                for p in page_set:
                    try:
                        index = pages.index(p, i + 1)
                    except ValueError:
                        index = float('inf')  # Page not found in the future
                    if index > farthest_index:
                        farthest_index = index
                        farthest_page = p
                page_set.remove(farthest_page)
                page_set.add(page)
            page_faults += 1

    return page_faults


import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        tokens = f.read().split()

    k = int(tokens[0])
    m = int(tokens[1])
    pages = list(map(int, tokens[2:2 + m]))

    print(f"FIFO  : {fifo(pages, k)}")
    print(f"LRU   : {lru(pages, k)}")
    print(f"OPTFF : {optff(pages, k)}")

if __name__ == "__main__":
    main()