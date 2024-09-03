import matplotlib.pyplot as plt

def plot_language_stats(language_stats):
    """Plots a horizontal bar chart showing the usage of different programming languages
    with a color-coded legend next to the bar chart.
    
    Args:
        language_stats: A dictionary where keys are language names and values are usage counts.
    """

    # Sort languages by usage in descending order
    sorted_languages = sorted(language_stats.items(), key=lambda item: item[1], reverse=True)
    labels = [item[0] for item in sorted_languages]
    sizes = [item[1] for item in sorted_languages]

    # Normalize sizes to percentage of the total
    total_size = sum(sizes)
    sizes_percentage = [size / total_size * 100 for size in sizes]

    # Define a color map to assign unique colors to each language
    cmap = plt.get_cmap("tab20")  # This colormap supports a large number of distinct colors
    colors = [cmap(i % 20) for i in range(len(labels))]

    # Create the horizontal bar chart
    fig, ax = plt.subplots(figsize=(14, 10))  # Increase width and height to accommodate the legend
    left = 0  # Starting position for the first bar segment
    for i, (size, label) in enumerate(zip(sizes_percentage, labels)):
        ax.barh(0, size, left=left, color=colors[i], edgecolor='white', height=0.5)  # Thin bar
        left += size

    # Remove y-axis and ticks
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    # Adjust the figure to leave space for the legend
    plt.subplots_adjust(left=0.1, right=0.6, top=0.9, bottom=0.1)

    # Create the dot-style legend next to the bar
    for i, (label, size) in enumerate(zip(labels, sizes_percentage)):
        plt.text(1.02, 0.9 - 0.025*i, '●', fontsize=10, color=colors[i], verticalalignment='center', horizontalalignment='right', transform=ax.transAxes)
        plt.text(1.05, 0.9 - 0.025*i, f'{label} {size:.2f}%', fontsize=10, verticalalignment='center', horizontalalignment='left', transform=ax.transAxes)

    # Set a title similar to the provided image
    plt.title('Most Used Languages', fontsize=16, color='blue', loc='left', pad=20)

    # Show the plot
    plt.show()

# Example usage with the full set of languages
language_stats = {
    'Java': 169954, 'Kotlin': 351, 'JavaScript': 1793498, 'HTML': 199984, 'CSS': 16315900, 'Arduino': 484654, 
    'C': 4983728, 'Shell': 1437649, 'C++': 21836927, 'Makefile': 204758, 'Objective-C': 23326, 'M4': 7672, 
    'Python': 15445650, 'Eagle': 3119989, 'TeX': 125325, 'CMake': 64619, 'Processing': 231311, 'QMake': 3735, 
    'MATLAB': 1069450, 'nesC': 472376, 'Pascal': 23592, 'Ruby': 4445, 'Roff': 91818, 'XSLT': 261112, 
    'AGS Script': 64518, 'Jupyter Notebook': 1902491, 'Assembly': 41378, 'TypeScript': 69266, 'HCL': 125, 
    'SystemVerilog': 65708, 'Stata': 873, 'Go': 474, 'VHDL': 81103, 'Tcl': 25269, 'Verilog': 6172, 
    'Mathematica': 455, 'Standard ML': 64, 'Fortran': 26, 'Scheme': 20, 'SCSS': 8625895, 'PowerShell': 1754, 
    'Nushell': 1700, 'Dockerfile': 146
}

plot_language_stats(language_stats)
