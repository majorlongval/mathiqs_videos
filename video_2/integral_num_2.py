from manim import *
import numpy as np


class integral_num_2(Scene):
    def construct(self):
        integralTex = MathTex(r"\int\frac{Ax + B}{Cx^2+D}dt")
        problemTex = Tex(
            r"Evalue the following indefinite integral \\where $A$, $B$, $C$ and $D$ are constants"
        ).next_to(integralTex, UP, buff=0.5)
        self.play(Write(problemTex))
        self.play(Write(integralTex))
        self.wait(4)
