import matplotlib.pyplot as plt
from matplotlib import animation
import random

# Time complexity: O(n log n)
# Space complexity: O(n)

def merge_sort(data, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from merge_sort(data, left, mid)
        yield from merge_sort(data, mid + 1, right)
        yield from merge(data, left, mid, right)
    yield data, left, right

def merge(data, left, mid, right):
    merged = []
    left_idx = left
    right_idx = mid + 1
    while left_idx <= mid and right_idx <= right:
        if data[left_idx] < data[right_idx]:
            merged.append(data[left_idx])
            left_idx += 1
        else:
            merged.append(data[right_idx])
            right_idx += 1
    while left_idx <= mid:
        merged.append(data[left_idx])
        left_idx += 1
    while right_idx <= right:
        merged.append(data[right_idx])
        right_idx += 1
    for i, value in enumerate(merged):
        data[left + i] = value
        yield data, left + i, -1
    yield data, -1, right
    
def update_plot(data_info, bars):
    data, idx1, idx2 = data_info
    for i, bar in enumerate(bars):
        if i == idx1 or i == idx2:
            bar.set_color('red')
        else:
            bar.set_color('blue')
        bar.set_height(data[i])

def visualize_merge_sort(data, interval = 1):
    fig, ax = plt.subplots()
    ax.set_title('Merge Sort Visualization')
    bars = ax.bar(range(len(data)), data, align='center', color='blue')

    anim = animation.FuncAnimation(fig, update_plot, frames=merge_sort(data, 0, len(data) - 1), fargs=(bars,), interval=interval, repeat=False)
    plt.show()
    
def main():
    n = 200
    data = [random.randint(1, 1000) for _ in range(n)]
    visualize_merge_sort(data, interval=1)

if __name__ == "__main__":
    main()