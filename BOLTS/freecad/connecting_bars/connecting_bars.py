# **************************************************************************************
# *                                                                                    *
# *    BOLTS - Open Library of Technical Specifications                                *
# *                                                                                    *
# *    Copyright (c) 2014 Fabrizio Pollastri <f.pollastri@inrim.it>                    *
# *                                                                                    *
# *    This library is free software; you can redistribute it and/or                   *
# *    modify it under the terms of the GNU Lesser General Public                      *
# *    License as published by the Free Software Foundation; either                    *
# *    version 2.1 of the License, or any later version.                               *
# *                                                                                    *
# *    This library is distributed in the hope that it will be useful,                 *
# *    but WITHOUT ANY WARRANTY; without even the implied warranty of                  *
# *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU                *
# *    Lesser General Public License for more details.                                 *
# *                                                                                    *
# *    You should have received a copy of the GNU Lesser General Public                *
# *    License along with this library; if not, write to the Free Software             *
# *    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA    *
# *                                                                                    *
# **************************************************************************************


from FreeCAD import Base
import Part

from math import pi


def tube_bar_crimped_ends(params, document):
    id = params["id"]
    od = params["od"]
    cg = params["cg"]
    hd = params["hd"]
    cl = params["cl"]
    rl = params["rl"]
    tl = params["tl"]
    sd = params["sd"]
    name = params["name"]

    part = document.addObject("Part::Feature", "BOLTS_part")
    part.Label = name

    # ********* round to crimped transition *********

    def oval(pm, tn, y, z):
        """ Return an oval wire with given perimeter *pm* and thickness *tn*,
        centered at 0, *y*, *z*. The oval plane is parallel to the xy plane
        and the oval has its long axis parallel to y axis. """

        # half thickness
        htn = 0.5 * tn

        # half width of flat part
        hfw = 0.25 * (pm - pi * tn)

        # control points
        p1 = Base.Vector(-hfw, htn + y, z)
        p2 = Base.Vector(+hfw, htn + y, z)
        p3 = Base.Vector(+htn + hfw, y, z)
        p4 = Base.Vector(+hfw, -htn + y, z)
        p5 = Base.Vector(-hfw, -htn + y, z)
        p6 = Base.Vector(-htn - hfw, y, z)

        # return oval wire
        return Part.Wire(Part.Shape([
            Part.Line(p1, p2),
            Part.Arc(p2, p3, p4),
            Part.Line(p4, p5),
            Part.Arc(p5, p6, p1)]).Edges)

    # if requested, shift along y from origin for side crimped oval
    if sd:
        dy = (id - cg) / 2.0
    else:
        dy = 0.0

    # inner part
    round_i1 = Part.Wire(Part.makeCircle(0.5 * id))
    dv = Base.Vector(0.0, 0.0, 0.02 * tl)
    dvn = Base.Vector(0.0, 0.0, -0.02 * tl)
    round_i2 = round_i1.copy()
    round_i2.translate(dv)
    crimped_i1 = oval(pi * id, cg, dy, tl)
    crimped_i2 = crimped_i1.copy()
    crimped_i2.translate(dvn)
    trans_i = Part.makeLoft([round_i1, round_i2, crimped_i2, crimped_i1], True)

    # outer part
    round_o1 = Part.Wire(Part.makeCircle(0.5 * od))
    round_o2 = round_o1.copy()
    round_o2.translate(dv)
    tn_o = cg + od - id
    crimped_o1 = oval(pi * od, tn_o, dy, tl)
    crimped_o2 = crimped_o1.copy()
    crimped_o2.translate(dvn)
    trans_o = Part.makeLoft([round_o1, round_o2, crimped_o2, crimped_o1], True)

    # ********* crimped parts *********
    eaxis = Base.Vector(0.0, 0.0, cl)
    crimped_i = Part.Face(crimped_i1).extrude(eaxis)
    crimped_o = Part.Face(crimped_o1).extrude(eaxis)

    # ********* fastening hole *********
    oxyz = Base.Vector(0.0, -0.5 * tn_o + dy, tl + 0.5 * cl)
    haxis = Base.Vector(0.0, 1.0, 0.0)
    hole = Part.makeCylinder(0.5 * hd, tn_o, oxyz, haxis)

    # ********* combine the parts forming one end *********

    # join transitions and crimped parts
    end_i = trans_i.fuse(crimped_i)
    end_o = trans_o.fuse(crimped_o)

    # one end: make the inner part the void part of the outer part.
    end_a = end_o.cut(end_i).removeSplitter()

    # make the fastening hole
    end_a = end_a.cut(hole).removeSplitter()

    # ********* the other end *********
    end_b = end_a.copy()
    p0 = Base.Vector(0.0, 0.0, 0.0)
    end_b.rotate(p0, haxis, 180.0)
    end_b.translate(Base.Vector(0.0, 0.0, -rl))

    # ********* the central pipe *********
    caxis = Base.Vector(0.0, 0.0, -1)
    pipe_o = Part.makeCylinder(0.5 * od, rl, p0, caxis)
    pipe_i = Part.makeCylinder(0.5 * id, rl, p0, caxis)
    pipe = pipe_o.cut(pipe_i).removeSplitter()

    # ********* all together *********
    part.Shape = end_a.fuse(end_b).fuse(pipe)
