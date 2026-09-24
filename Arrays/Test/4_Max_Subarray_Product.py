def maxProduct(arr):
    max_product = arr[0]
    min_product = arr[0]
    overall_max = arr[0]

    for i in range(1, len(arr)):
        old_max = max_product
        old_min = min_product

        new_max = max(
            arr[i],
            arr[i] * old_max,
            arr[i] * old_min
        )

        new_min = min(
            arr[i],
            arr[i] * old_max,
            arr[i] * old_min
        )

        max_product = new_max
        min_product = new_min

        overall_max = max(overall_max, max_product)

    return overall_max

