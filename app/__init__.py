import sys
import tui
import display_statistics
import visuals

"""
Created May 2021

Purpose: The main script to navigate the program

@author Oliver Køppen, s175108
"""

data = None
aggregated_data = None

while True:
    """
    The main loop controlling the navigation of the script
    """

    selected_item = tui.startMenu(data)

    if selected_item == 1: # load / reload data
        aggregated_data = None
        data = tui.loadDataMenu()
    elif selected_item == 2: # aggregate
        aggregated_data = tui.aggregateDataMenu(data) or None
    elif selected_item == 3: # print statistics
        statistics = aggregated_data if aggregated_data is not None else data  # We know data is always present at this point
        display_statistics.print_statistics(statistics[0], statistics[1])
    elif selected_item == 4: # visualize plots
        tui.visualsMenu(aggregated_data or data)
    elif selected_item == 9: # exit
        print("System is exiting.")
        sys.exit(0)
