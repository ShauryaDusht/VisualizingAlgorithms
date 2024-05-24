from random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            yield data, j, j + 1, -1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                yield data, j, j + 1, -1
        yield data, -1, -1, n - i - 1
        if not swapped:
            for k in range(n - i - 1, -1, -1):
                yield data, -1, -1, k
            break
    for i in range(n):
        yield data, -1, -1, i

def update_plot(data_info, bars):
    data, idx1, idx2, sorted_idx = data_info
    for i, bar in enumerate(bars):
        if i == idx1 or i == idx2:
            bar.set_color('red')
        elif i > sorted_idx:
            bar.set_color('green')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_bubble_sort(data):
    fig, ax = plt.subplots()
    ax.set_title('Bubble Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')

    anim = animation.FuncAnimation(fig, update_plot, frames=bubble_sort(data), fargs=(bars,), repeat=False)
    plt.show()
    
def main():
    # Number of elements
    n = 30
    # Generate random data from 0 to 100
    data = [int(random() * 100) for _ in range(n)]
    visualize_bubble_sort(data)

if __name__ == "__main__":
    main()
