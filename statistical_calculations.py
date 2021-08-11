def col_index(data, col_name):
    return np.where(data[0] == col_name)


def outlier_pct(data, col_name):
    
    index = col_index(data, col_name)
    
    try:
        col = data[1:, index].astype('float')
    except Exception as e:
        print("cannot be converted to float")
        print(e)

    max_thresold = np.percentile(col, 99)
    min_threshold = np.percentile(col, 1) 
    no_outliers = [y for y in col.tolist() if y >= min_threshold and y <= max_thresold]

    out_perct = ((len(col)-len(no_outliers))/len(col))*100
    return round(out_perct,2)

def display(data, col_name):
    width = [i for i in range(1, len(data))]
    index = col_index(data, col_name)
    values = data[1:, index].astype("float")
    plt.title(col_name)
    plt.ylim(min(values) , max(values))
    plt.scatter(x=width, y=values,alpha=0.15)
    plt.hlines(y=np.mean(values), xmin=0, xmax=len(data[1:,0]), colors='r')
    plt.show()
