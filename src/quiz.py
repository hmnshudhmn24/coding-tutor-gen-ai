def generate_quiz(concept: str):
    if concept.lower() == "binary search":
        return ("What is the time complexity of Binary Search?", ["O(n)", "O(log n)", "O(n log n)"], 1)
    elif concept.lower() == "recursion":
        return ("Which keyword is essential for recursion in Python?", ["loop", "def", "return"], 2)
    else:
        return (f"What is a key property of {concept}?", ["Option A", "Option B", "Option C"], 0)
