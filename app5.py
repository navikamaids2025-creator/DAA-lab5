import streamlit as st
import random

comparison_count = 0


def min_max_dc(arr, low, high):
    global comparison_count

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


def min_max_naive(arr):
    mn = mx = arr[0]
    comparisons = 0

    for x in arr[1:]:
        comparisons += 1
        if x < mn:
            mn = x

        comparisons += 1
        if x > mx:
            mx = x

    return mn, mx, comparisons


st.title("Divide and Conquer - Min & Max Finder")

st.write("Enter integers separated by commas.")

user_input = st.text_input(
    "Array",
    "3,1,7,4,9,2,8,5,6,0"
)

if st.button("Find Min and Max"):

    try:
        arr = [int(x.strip()) for x in user_input.split(",")]

        if len(arr) == 0:
            st.error("Please enter at least one number.")

        else:
            comparison_count = 0

            minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
            dc = comparison_count

            _, _, naive = min_max_naive(arr)

            st.success("Results")

            st.write("### Output")
            st.write(f"Array: {arr}")
            st.write(f"Minimum: **{minimum}**")
            st.write(f"Maximum: **{maximum}**")
            st.write(f"D&C Comparisons: **{dc}**")
            st.write(f"Naive Comparisons: **{naive}**")

    except:
        st.error("Please enter only integers separated by commas.")

st.divider()

st.subheader("Performance Analysis")

sizes = [10, 100, 1000, 10000]

table = []

for size in sizes:

    arr = [random.randint(1, 10000) for _ in range(size)]

    comparison_count = 0
    min_max_dc(arr, 0, len(arr) - 1)
    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = (3 * size) // 2 - 2

    table.append({
        "Size": size,
        "D&C Comparisons": dc,
        "Naive Comparisons": naive,
        "Formula (3n/2-2)": formula
    })

st.table(table)
