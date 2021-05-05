"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util
import searches
import graphics.Engine


# This is the base of the project

class run:
    searches.stats_var = "id"
    searches.AorD_var = True
    searches.type1_var = "Grass"
    searches.type2_var = "Poison"
    searches.gen_var = 1
    searches.Legendary_var = False
    searches.poke_name = None

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

        type1_var = s.readline()
        type2_var = s.readline()
        gen_var = s.readline()
        Legendary_var = s.readline()
        stats_var = s.readline()
        AorD_var = s.readline()

        a = util.search()
        a = a.getList(stats_var, AorD_var, [type1_var, type2_var, gen_var, Legendary_var])
        print(a)

        b = util.search()
        b = b.getList("id", False, ["Poison", "All", 1, False])
        print(b)
