def ecdf(data):
    """
    Args - data: DataFrame
    Function: Plots ECDF
    """
    # Number of data points: nums
    nums = len(data)

    # x-axis data
    x = np.sort(data)

    # y-axis data
    y = np.arange(1, n+1) / n

    plt.plot(x, y, marker='.', linestyle='none')
