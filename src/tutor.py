def explain_concept(concept: str) -> str:
    explanations = {
        "binary search": "Binary Search is a divide-and-conquer algorithm. It works by repeatedly dividing the sorted array in half until the target element is found.",
        "recursion": "Recursion is when a function calls itself with smaller inputs, typically with a base case to stop."
    }
    return explanations.get(concept.lower(), f"Here’s a simplified explanation of {concept}.")
