#           Linear search algo.
import time
import matplotlib.pyplot as plt

def draw_data(arr, color_array, delay=0.05, algo_num=0):
    plt.clf()  # Clear the previous plot
    # plt.xlabel(arr)
    plt.title('Linear Search Algo')
    plt.bar(range(len(arr)), arr, color=color_array, width=0.1)
    wnd = plt.get_current_fig_manager()
    # Set the window resolution and position
    wnd.window.wm_geometry(f"600x400+40+40")
    plt.pause(delay)  # Pause for the animation


def linear_search(arr, delay=0, target=1, draw_data=None, pause_event=None):
    for index in range(len(arr)):

        if pause_event:
            while pause_event.is_set():
                time.sleep(0.1)

        while pause_event.is_set():
            time.sleep(0.1)

        if draw_data:
            draw_data(arr, ['red' if x == index else 'blue' for x in range(len(arr))])

        if arr[index] == target:
            if draw_data:
                draw_data(arr, ['green' if x == index else 'blue' for x in range(len(arr))])
            return index

    if draw_data:
        draw_data(arr, ['blue' for x in range(len(arr))])

    return -1
