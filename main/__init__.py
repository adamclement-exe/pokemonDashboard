"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util
import graphics.Engine

# This is the base of the project

class run:

    def __init__(self):
        Devs = ("Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")


        points = [[-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1], [1, -1, -1], [1, -1, 1], [1, 1, 1], [1, 1, -1]]
        triangles = [[0, 1, 2], [0, 2, 3], [2, 3, 7], [2, 7, 6], [1, 2, 5], [2, 5, 6], [0, 1, 4], [1, 4, 5], [4, 5, 6],
                     [4, 6, 7], [3, 7, 4], [4, 3, 0]]

        test = graphics.Engine.Engine3D(points, triangles, title='Cube')
        def animation():
            test.clear()
            test.rotate('y', 0.1)
            test.rotate('x', 0.1)
            test.render()
            test.screen.after(1, animation)

        animation()
        test.screen.window.mainloop()

    def name_search(self):
        s = open("searches.txt", "r")
        pokename_var = s.readline()

        print(pokename_var)

    def refract_search(self):
        s = open("searches.txt", "r")
        var = s.readline()
        var = (var[:-1]).split(",")

        type1_var = str(var[0])
        type2_var = str(var[1])
        stats_var = var[4]

        gen_var = str(var[2])
        if gen_var != 'All':
            gen_var = int(var[2])

        Legendary_var = str(var[3])
        if Legendary_var == "False":
            Legendary_var = False
        elif Legendary_var == "True":
            Legendary_var = True

        AorD_var = str(var[5])
        if AorD_var == "False":
            AorD_var = False
        elif AorD_var == "True":
            AorD_var = True

        a = util.search()
        a = a.getList(stats_var, AorD_var, [type1_var, type2_var, gen_var, Legendary_var])  # filtered search
        print(a)
