import matplotlib.pyplot as plt
from matplotlib import animation
from random import randint

# Time complexity: O(n log n)
# Space complexity: O(log n)
## Unstable

def quick_sort(data, low, high):
    if low < high:
        pivot = yield from partition(data, low, high)
        yield from quick_sort(data, low, pivot - 1)
        yield from quick_sort(data, pivot + 1, high)
    yield data, low, high

def partition(data, low, high):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            yield data, i, j
    data[i + 1], data[high] = data[high], data[i + 1]
    yield data, i + 1, high
    return i + 1

def update_plot(data_info, bars):
    data, left, right = data_info
    for i, bar in enumerate(bars):
        if i == left or i == right:
            bar.set_color('red')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_quick_sort(data, interval=1):
    fig, ax = plt.subplots()
    ax.set_title('Quick Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')
    
    anim = animation.FuncAnimation(fig, update_plot, frames=quick_sort(data, 0, len(data) - 1), fargs=(bars,), interval=interval, repeat=False)
    plt.show()

def main():
    n = 100
    data = [randint(0, 100) for _ in range(n)]
    visualize_quick_sort(data, interval=10) 

if __name__ == "__main__":
    main()
