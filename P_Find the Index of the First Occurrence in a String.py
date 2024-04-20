def str(haystack, needle):
    try:
        return haystack.index(needle)
    except ValueError:
        return -1
    
# Test
haystack = "sadbutsad"
needle = "sad"
print(str(haystack, needle))  # Output: 0