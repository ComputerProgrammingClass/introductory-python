shapes = ["circle", "triangle"]

shapes.append("rectangle")
shapes.append("rectangle")
shapes.append("rectangle")
shapes.append("rectangle")

print(shapes)

shapes.remove("rectangle")
shapes.remove("rectangle")
shapes.remove("rectangle")

print(shapes)

print("There are", shapes.count("rectangle"), "rectangles in our list")
print("There are", shapes.count("triangle"), "triangle in our list")
