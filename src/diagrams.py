from graphviz import Digraph

def generate_diagram(concept: str):
    if concept.lower() == "binary search":
        dot = Digraph()
        dot.node("A", "Start")
        dot.node("B", "Check Mid")
        dot.node("C", "Search Left Half")
        dot.node("D", "Search Right Half")
        dot.edges(["AB", "BC", "BD"])
        path = "/mnt/data/binary_search.png"
        dot.render(path, format="png", cleanup=True)
        return path
    return None
