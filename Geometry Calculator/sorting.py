#sort by area
def sort_area(shapes):
    return sorted(shapes, key=lambda s: s.area, reverse=True)
#sort by perimeter
def sort_perim(shapes):
    return sorted(shapes, key=lambda s: s.perimeter, reverse=True)
#compares the areas
def comp_area(s1, s2):
    if s1.area > s2.area:
        return s1
    elif s2.area > s1.area:
        return s2
    else:
        return "Tie"
#compares the perimeters
def comp_perim(s1, s2):
    if s1.perimeter > s2.perimeter:
        return s1
    elif s2.perimeter > s1.perimeter:
        return s2
    else:
        return "Tie"
#lets them choose the shapesies
def choose_shape(shapes):
    for i, s in enumerate(shapes):
        print(f"{i + 1}: {s.__str__().splitlines()[0]}")
    index = int(input("Select shape by number: ")) - 1
    return shapes[index]
#main function to sort the shapes
def sort_main(rects, tris, circs):
    while True:
        print("\n1. Sort Rectangles")
        print("2. Sort Triangles")
        print("3. Sort Circles")
        print("4. Compare Two Shapes")
        print("5. Go Back")
        #lets them choose which shape they want to do
        choice = input("Choose an option: ").strip()
        #does the corresponding actions for the choices
        if choice == '1':
            sort_type = input("Sort by (area/perimeter): ").strip().lower()
            if sort_type == 'area':
                sorted_list = sort_area(rects)
            else:
                sorted_list = sort_perim(rects)
            for s in sorted_list:
                print(s)
        elif choice == '2':
            sort_type = input("Sort by (area/perimeter): ").strip().lower()
            if sort_type == 'area':
                sorted_list = sort_area(tris)
            else:
                sorted_list = sort_perim(tris)
            for s in sorted_list:
                print(s)
        elif choice == '3':
            sort_type = input("Sort by (area/perimeter): ").strip().lower()
            if sort_type == 'area':
                sorted_list = sort_area(circs)
            else:
                sorted_list = sort_perim(circs)
            for s in sorted_list:
                print(s)
        elif choice == '4':
            shapes = rects + tris + circs
            if len(shapes) < 2:
                print("Need at least two shapes to compare.")
                continue
            print("Choose the first shape:")
            s1 = choose_shape(shapes)
            print("Choose the second shape:")
            s2 = choose_shape(shapes)
            if s1 == s2:
                print("Choose two different shapes.")
                continue
            compare_by = input("Compare by (area/perimeter): ").strip().lower()
            if compare_by == 'area':
                result = comp_area(s1, s2)
            else:
                result = comp_perim(s1, s2)
            print("Result:", result)
        elif choice == '5':
            break
        else:
            print("Invalid input.")