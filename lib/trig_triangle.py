from manim import (
    Point,
    MathTex,
    VGroup,
    DEFAULT_FONT_SIZE,
    DEFAULT_STROKE_WIDTH,
    Angle,
    SMALL_BUFF,
    DOWN,
    LEFT,
    Polygon,
    Line,
    AnimationGroup,
    Create,
    Write,
    UP,
    RIGHT,
)

DEFAULT_TRIANGLE_DIMENSIONALITY = DTD = 3
DEFAULT_ANCHOR_POINT = Point([0, 0, 0])
DEFAULT_ADJ_TEX = MathTex("a")
DEFAULT_OPP_TEX = MathTex("b")
DEFAULT_HYP_TEX = MathTex("\sqrt{a^2+b^2}")


class TrigTriangle(VGroup):
    def __init__(
        self,
        dim=DTD,
        anchor_point=DEFAULT_ANCHOR_POINT,
        adj_tex=DEFAULT_ADJ_TEX,
        opp_tex=DEFAULT_OPP_TEX,
        hyp_tex=DEFAULT_HYP_TEX,
        **kwargs
    ):
        super().__init__(**kwargs)
        self._dim = dim
        self._x0 = anchor_point.get_x()
        self._y0 = anchor_point.get_y()
        self._ratio = self._dim / DTD
        self._adj_tex = adj_tex.set(font_size=DEFAULT_FONT_SIZE * self._ratio)
        self._opp_tex = opp_tex.set(font_size=DEFAULT_FONT_SIZE * self._ratio)
        self._hyp_tex = hyp_tex.set(font_size=DEFAULT_FONT_SIZE * self._ratio)
        self._triangle = Polygon(
            [self._x0, self._y0, 0],
            [self._x0, self._y0 + self._ratio * 2, 0],
            [self._x0 + self._dim, self._y0, 0],
        )
        self._triangle.set(stroke_width=self._ratio * DEFAULT_STROKE_WIDTH)
        self._line1 = Line(
            [self._x0 + self._dim, self._y0, 0],
            [self._x0, self._y0 + self._ratio * 2, 0],
        )
        self._line2 = Line(
            [self._x0, self._y0, 0], [self._x0, self._y0 + self._ratio * 2, 0]
        )
        self._line3 = Line([self._x0 + self._dim, self._y0, 0], [self._x0, self._y0, 0])
        self._angle = Angle(
            self._line1,
            self._line3,
            radius=self._ratio,
            dot=False,
            stroke_width=self._ratio * DEFAULT_STROKE_WIDTH,
        )
        self._theta = MathTex(
            r"\theta", font_size=DEFAULT_FONT_SIZE * self._ratio
        ).move_to(
            Angle(
                self._line1, self._line3, radius=self._ratio * (1 + 3 * SMALL_BUFF)
            ).point_from_proportion(0.5)
        )

        self._adj_tex.next_to(self._line3, self._ratio * 0.2 * DOWN, buff=0.5)
        self._opp_tex.next_to(self._line1, self._ratio * 0.2 * LEFT, buff=0.5)
        self._hyp_tex.next_to(
            self._line1.get_center(), self._ratio * 0.2 * (UP + RIGHT), buff=0.5
        )

    def animate(self):
        return AnimationGroup(
            Create(self._triangle),
            Create(self._angle),
            Write(self._theta),
            Write(self._adj_tex),
            Write(self._opp_tex),
            Write(self._hyp_tex),
        )

    def items(self):
        return VGroup(
            self._triangle,
            self._angle,
            self._theta,
            self._adj_tex,
            self._opp_tex,
            self._hyp_tex,
        )
