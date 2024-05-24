from random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            yield data, min_idx, j, -1
            if data[j] < data[min_idx]:
                min_idx = j
                yield data, min_idx, j, -1
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            yield data, i, min_idx, -1
    for i in range(n):
        yield data, -1, -1, i

def update_plot(data_info, bars):
    data, min_idx, idx, sorted_idx = data_info
    for i, bar in enumerate(bars):
        if i == min_idx or i == idx:
            bar.set_color('red')
        elif i > sorted_idx:
            bar.set_color('green')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_selection_sort(data):
    fig, ax = plt.subplots()
    ax.set_title('Selection Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')

    anim = animation.FuncAnimation(fig, update_plot, frames=selection_sort(data), fargs=(bars,), repeat=False)
    plt.show()

def main():
    # Number of elements
    n = 10
    # Generate random data from 0 to 100
    data = [int(random() * 100) for _ in range(n)]
    visualize_selection_sort(data)

if __name__ == "__main__":
    main()
