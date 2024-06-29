import matplotlib.pyplot as plt
from matplotlib import animation
from random import randint

# Time complexity: O(n log n)
# Space complexity: O(1)
## Unstable

def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        yield data, i, largest
        yield from heapify(data, n, largest)

def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        yield data, i, 0
        yield from heapify(data, i, 0)
    yield data, -1, -1

def update_plot(data_info, bars):
    data, idx1, idx2 = data_info
    for i, bar in enumerate(bars):
        if i == idx1 or i == idx2:
            bar.set_color('red')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_heap_sort(data, interval=1):
    fig, ax = plt.subplots()
    ax.set_title('Heap Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')

    anim = animation.FuncAnimation(fig, update_plot, frames=heap_sort(data), fargs=(bars,), interval=interval, repeat=False)
    plt.show()

def main():
    n = 100
    data = [randint(0, 100) for _ in range(n)]
    visualize_heap_sort(data, interval=10)

if __name__ == "__main__":
    main()