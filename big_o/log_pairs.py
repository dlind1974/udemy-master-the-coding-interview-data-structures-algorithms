def log_pairs(array):
    pair_count = 0
    for i in range(len(array)):  # O(n)
        for j in range(len(array)):  # O(n)
            if j != i:
                print(array[i], array[j])
                pair_count += 1
    print(f"pair_count: {pair_count}")


if __name__ == "__main__":
    boxes = [1, 2, 3, 4, 5];
    log_pairs(boxes)
    # O(n) * O(n) = O(n*n) = O(n^2)
