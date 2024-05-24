from random import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            yield data, i, j, i - 1
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        yield data, i, j, i - 1
    for k in range(len(data)):
        yield data, -1, -1, k

def update_plot(data_info, bars):
    data, idx1, idx2, sorted_idx = data_info
    for i, bar in enumerate(bars):
        if i == idx1 or i == idx2:
            bar.set_color('red')
        elif i <= sorted_idx:
            bar.set_color('green')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_insertion_sort(data):
    fig, ax = plt.subplots()
    ax.set_title('Insertion Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')

    anim = animation.FuncAnimation(fig, update_plot, frames=insertion_sort(data), fargs=(bars,), repeat=False)
    plt.show()
    
def main():
    # Number of elements
    n = 30
    # Generate random data from 0 to 100
    data = [int(random() * 100) for _ in range(n)]
    visualize_insertion_sort(data)

if __name__ == "__main__":
    main()