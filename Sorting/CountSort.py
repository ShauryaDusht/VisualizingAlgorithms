import matplotlib.pyplot as plt
from matplotlib import animation
from random import randint

# Time complexity: O(n + k)
# Space complexity: O(n + k)

def count_sort(data):
    n = len(data)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        count[data[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        output[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        i -= 1
        yield output, i
    yield output, -1

def update_plot(data_info, bars):
    data, idx = data_info
    for i, bar in enumerate(bars):
        if i == idx:
            bar.set_color('red')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])
    
def visualize_count_sort(data, interval=1):
    fig, ax = plt.subplots()
    ax.set_title('Count Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')
    
    anim = animation.FuncAnimation(fig, update_plot, frames=count_sort(data), fargs=(bars,), interval=interval, repeat=False)
    plt.show()
    
def main():
    n = 100
    data = [randint(0, 9) for _ in range(n)]
    visualize_count_sort(data, interval=10)

if __name__ == "__main__":
    main()