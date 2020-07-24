Please add your answers to the Analysis of Algorithms exercises here.
Exercise I

a) O(n): The loop will run n times.

b) O(n log n): The loop will run n \* (a value that is logarithmically proportional to n) times.

c) O(n + 1): The loop will run n + 1 times.
Exercise II

Lowest number of broken eggs def find_floor(n):

    f = 1
    while f < n:
        if egg does not break:
            f += 1
        else: - return f return "Buildint too short to break egg"

Algorithm is O(n) complexity because it will in a worst case scinerio run a loop n times. The number of dropped will be higher because you are essentiall iterating through the building, but will never break more than 1 egg.

def find_floor(n):

    high = n

    low = 1

    thrown = {}

    confirmed = False

    while confirmed == False:
        mid = high + low // 2
        if mid thrown egg breaks and mid - 1 in thrown and thrown[mid-1] == whole:
            confirmed = True
            return mid
        elif mid thrown egg != break and mid + 1 in thrown and thrown[mid+1] == broken:.
            confirmed = True
            return mid + 1
        elif mid thrown egg breaks and mid - 1 not in thrown:
            thrown[mid] = broken
            high = mid
        elif mid thrown egg != break and mid + 1 not in thrown:
            thrown[mid] = whole
            low = mid + 1
        else:
            confirmed = True
            return "Building too short."

Note: thrown dictionary used to make algorithm O(log2n) rather than O(log2n + c).

Algorithm is O(log2n) since the loop will run log2 n times in the worst case scinerio. While the overall number of eggs dropped will be lower, the number of those eggs that will break is higher in the worst case scinerio. In a worst case scinerio this solution will have log2n \* 2 for dropped + broken eggs which will still be lower than n.
