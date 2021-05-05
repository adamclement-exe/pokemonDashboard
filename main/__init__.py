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
        a = util.search()
        a = a.getList("id", False, ["All", "Electric", "All", "All", "All", "All", "All", "All", "All", 1, False])
        print(a)

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
        instance = util.csv_loader("Pokemon.csv")
        d = instance.sort("id", True)
        pokename = instance.refactor_list(d, "name", searches.poke_name)
        print(pokename)

    def refract_search(self):
        instance = util.csv_loader("Pokemon.csv")
        #  following code filters the users search
        d = instance.sort(searches.stats_var, searches.AorD_var)
        print('d', d)
        t1 = instance.refactor_list(d, "type1", searches.type1_var)
        print('t1', t1)
        t2 = instance.refactor_list(t1, "type2", searches.type2_var)
        print('t2', t2)
        gen = instance.refactor_list(t2, "Generation", searches.gen_var)
        leg = instance.refactor_list(gen, "Legendary", searches.Legendary_var)
        searches_list = leg

        print(searches_list)


run()
