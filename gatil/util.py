# ada.gatil.util.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Projeto sem descrição, (mude esta linha).

.. codeauthor:: Nome Sobrenome <mail@local.tipo>

Changelog
---------
.. versionadded::    22.03
        Descreva o que você adicionou no código.

"""
from _spy.vitollino.main import STYLE, Elemento, Point, CURSOR_STYLE, CURSOR_ELEMENT, _PATTERN



class Cursor(Elemento:
    def __init__(self, img, **kwargs):
        super().__init__(img, **kwargs)
        outer = self

        class Noop:
            def __init__(self):
                self.outer = outer

            def change(self, ev):
                pass

            @staticmethod
            def update_style(styler, new_style, delta=None):
                cur_style = dict(outer.style)
                '''
                point = Point(outer.alvo.style.left, outer.alvo.style.top)
                delta = delta if delta else Point(outer.alvo.style.width, outer.alvo.style.minHeight)
                print("delta.x, delta.y", outer.elt.style.left, outer.elt.style.top, delta.x, delta.y)
                cur_style.update(cursor=styler, left=point.x, top=point.y, width=delta.x, height=delta.y, **new_style)

                '''
                cur_style.update(cursor=styler, **new_style)
                #cur_style["min-height"] = "{}px".format(delta.y)
                return cur_style

            def next(self, ev):
                ev.target.style = self.update_style("move", _PATTERN.BCROSS)
                outer.current = outer.move

            def mouse_over(self, ev):
                ev.target.style.cursor = "default"

            def mouse_down(self, ev):
                outer.ponto = Point(ev.x, ev.y)
                outer.cursor = outer.current
                pass

            def mouse_move(self, ev):
                pass

            def mouse_up(self, _):
                outer.cursor = outer.noop
                #st = self.outer.elt.style
                #width_, height_, left_, top_ = st.width, st.minHeight, st.left, st.top
                #self.outer.elt.title = CURSOR_ELEMENT.format(left_, top_, width_, height_)
                outer.tit = CURSOR_ELEMENT.format(outer.x, outer.y, outer.w, outer.h)

        class Move(Noop):
            def mouse_move(self, ev):
                # delta = Point(int(alvo.style.left.rstrip("px")), int(alvo.style.top.rstrip("px"))) \
                delta = Point(outer.x, outer.y) + Point(ev.x, ev.y) - outer.ponto
                        
                outer.x, outer.y = delta
                #outer.elt.left, outer.elt.top = delta
                outer.ponto = Point(ev.x, ev.y)

            def mouse_over(self, ev):
                ev.target.style.cursor = "move"

            def next(self, ev):
                print("next resize")
                ev.target.style = self.update_style("grab", _PATTERN.BOKEH)
                outer.current = outer.resize

        class Resize(Noop):
            def mouse_move(self, ev):
                #delta = Point(int(outer.elt.style.width.rstrip("px")), int(outer.elt.style.minHeight.rstrip("px"))) \
                #        + Point(ev.x, ev.y) - outer.ponto
                delta = Point(outer.w, outer.h) + Point(ev.x, ev.y) - outer.ponto
                outer.w, outer.h = delta.px()
                # alvo.style = self.update_style("default", {}, delta)
                # outer.elt.style = self.update_style("default", PATTERN.BOKEH, delta)
                # print("mouse_move", alvo.style.minHeight, delta)
                outer.ponto = Point(ev.x, ev.y)

            def mouse_over(self, ev):
                ev.target.style.cursor = "grab"

            def next(self, ev):
                print("next noop")
                ev.target.style = self.update_style("default", _PATTERN.STARRY)
                outer.current = outer.noop

        def next_state(ev):
            # self.state.append(self.state.pop(0))
            self.current.next(ev)

        def _mouse_down(ev): return self.cursor.mouse_down(ev)

        def _mouse_up(ev): return self.cursor.mouse_up(ev)

        def _mouse_move(ev): return self.cursor.mouse_move(ev)

        def _mouse_over(ev): return self.cursor.mouse_over(ev)

        def _strip_kind(dm):
            kinds = "px %".split()
            kind = [k for k in kinds if isinstance(dm, str) and (k in dm)]
            # dm = str(dm) if isinstance(dm, int) else dm if isinstance(dm, str) else "0"
            return int(dm.rstrip(kind[0])) if kind else int(dm) if dm else 0

        self.noop, self.move, self.resize = self.state = [Noop(), Move(), Resize()]
        self.cursor = self.noop
        self.current = self.move
        # left, top = left + width//2 - 30, top + height//2 - 30
        cstyle = CURSOR_STYLE
        #cstyle = cstyle.format(width, height, height, left, top)
        #print("cstyle = ", cstyle)
        #cstyle = {k.strip(): v for k, v in (tp.split(":") for tp in cstyle.replace("\n", "").split(", ") if tp)}
        #style.update(**cstyle)
        style.update(**_PATTERN.STARRY)
        self.style = style
        self.elt = html.DIV(Id="__cursor__", style=style, title="")
        self.cena <= self.elt
        self.elt.onclick = next_state
        self.elt.onmousedown = _mouse_down
        self.elt.onmouseup = _mouse_up
        self.elt.onmousemove = _mouse_move
        self.elt.onmouseover = _mouse_over