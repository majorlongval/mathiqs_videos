from manim import *


class integral_num_1(Scene):
    def construct(self):
        problemTex = Tex(
            r"Evalue the following integral where $A$ and $\alpha$ are constants"
        )
        integralTex = Tex(r"$$\int\frac{A}{\alpha + \sqrt{t}}dt$$")

        miniproblemTex = Tex(r"Integral \\ to evaluate")
        problemTex.next_to(integralTex, UP, buff=0.5)
        self.play(Write(problemTex), run_time=1)
        self.play(Write(integralTex), run_time=2)
        self.add(integralTex)
        self.play(FadeOut(problemTex), run_time=0.5)
        miniproblemTex.move_to(Dot(UP * 3 + 5.2 * LEFT))
        self.play(
            Write(miniproblemTex),
            integralTex.animate.next_to(miniproblemTex, DOWN, buff=0.5),
        )

        framebox1 = SurroundingRectangle(integralTex, buff=0.1)
        self.play(Create(framebox1))
        step1 = Tex(
            r"Step 1: let $u = \sqrt{t}, \Rightarrow du = \frac{dt}{2\sqrt{t}}, \Rightarrow 2u \cdot du = dt$"
        )
        self.play(Write(step1.move_to(DOWN)))
        self.wait(4)
        step1Solved = Tex(r"$$\begin{aligned}u &=\sqrt{t},\\ 2udu &= dt\end{aligned}$$")
        step1Solved.next_to(integralTex, DOWN, buff=0.5)
        self.play(ReplacementTransform(step1, step1Solved))
        framebox2 = SurroundingRectangle(step1Solved, buff=0.1, color=BLUE)
        self.play(Create(framebox2))
        vg = VGroup().add(framebox1).add(framebox2)
        brace = Brace(vg, direction=[1, 0], sharpness=1)
        self.play(FadeIn(brace))
        step1Subbed = Tex(r"$$=\int\frac{A}{\alpha+u}2udu$$")
        step1Subbed_p2 = Tex(r"$$=A\int\frac{2u}{\alpha + u}du$$").next_to(brace, RIGHT)
        step1Subbed2 = Tex(
            r"$$\begin{aligned}&=A\int\frac{2u}{\alpha+u}du\\&u = \sqrt{t}\end{aligned}$$"
        ).next_to(framebox1, RIGHT, buff=0.5)
        step1Subbed.next_to(brace, RIGHT)
        self.play(Write(step1Subbed))
        self.wait(3)
        self.play(ReplacementTransform(step1Subbed, step1Subbed_p2))
        self.wait(2)
        self.play(
            FadeOut(framebox2, step1Solved, brace),
            ReplacementTransform(step1Subbed_p2, step1Subbed2),
        )

        step1_mini = Tex(r"Step 1 \\ $u$ sub").next_to(step1Subbed2, UP, buff=0.5)
        framebox3 = SurroundingRectangle(step1Subbed2, buff=0.1, color=BLUE)
        self.play(FadeIn(step1_mini, framebox3))
        step2 = Tex(
            r"Step 2: let $v = \alpha + u, \Rightarrow dv = du \: \text{and} \: u = v-\alpha$"
        )
        self.play(Write(step2.move_to(DOWN)))
        self.wait(4)
        step2_half = Tex(
            r"$$\begin{aligned} v &= \alpha + u \\ dv &= du \\ u &= v-\alpha\end{aligned}$$"
        ).next_to(framebox3, DOWN, buff=0.5)
        framebox4 = SurroundingRectangle(step2_half, buff=0.1, color=RED)
        self.play(ReplacementTransform(step2, step2_half), FadeIn(framebox4))
        vg = VGroup().add(framebox3, framebox4)
        brace = Brace(vg, direction=[1, 0], sharpness=1)
        self.play(FadeIn(brace))
        step2Subbed = [
            Tex(r"$$=A\int\frac{2\left(v-\alpha\right)}{v}dv$$").next_to(brace, RIGHT),
            Tex(r"$$=2A\int\frac{v-\alpha}{v}dv$$").next_to(brace, RIGHT),
            Tex(r"$$=2A\int\frac{v}{v}-\frac{\alpha}{v}dv$$").next_to(brace, RIGHT),
            Tex(r"$$=2A\left[\int dv -\alpha\int\frac{dv}{v}\right]$$").next_to(
                brace, RIGHT
            ),
            Tex(r"$$=2A\int dv -2A\alpha\int\frac{dv}{v}$$").next_to(brace, RIGHT),
        ]
        self.play(Write(step2Subbed[0]))
        self.wait(2)
        print(len(step2Subbed))
        for i in range(1, len(step2Subbed)):
            self.play(ReplacementTransform(step2Subbed[i - 1], step2Subbed[i]))
            self.wait(2)

        step2Subbed2 = Tex(
            r"$$\begin{aligned}&=2A\int dv -2A\alpha\int\frac{dv}{v}\\&v=\alpha+u\end{aligned}$$"
        ).next_to(framebox3, RIGHT, buff=0.5)
        self.play(
            FadeOut(framebox4, step2_half, brace),
            ReplacementTransform(step2Subbed[-1], step2Subbed2),
        )
        step2_mini = Tex(r"Step 2 \\ $v$ sub").next_to(step2Subbed2, UP, buff=0.5)
        framebox5 = SurroundingRectangle(step2Subbed2, buff=0.1, color=RED)
        self.play(FadeIn(step2_mini, framebox5))
        variables = VGroup(Tex("$A$"))
        finalStep = [
            Tex(
                r"Final Step: Evaluate the simplified integrals \\and substitute from $v$ to $t$"
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A\\int dv -2A\\alpha\\int\\frac{dv}{v}",
                "= 2Av -2A\\alpha\\ln\\left|v\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2Av -2A\\alpha\\ln\\left|v\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A(\\alpha+u) -2A\\alpha\\ln\\left|\\alpha+u\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A(\\alpha+\\sqrt{t}) -2A\\alpha\\ln\\left|\\alpha+\\sqrt{t}\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A\\alpha+2A\\sqrt{t} -2A\\alpha\\ln\\left|\\alpha+\\sqrt{t}\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A\\sqrt{t} -2A\\alpha\\ln\\left|\\alpha+\\sqrt{t}\\right| + C",
            ).move_to(DOWN),
            MathTex(
                "\\int\\frac{A}{\\alpha + \\sqrt{t}}dt",
                "= 2A\\left[\\sqrt{t} -\\alpha\\ln\\left|\\alpha+\\sqrt{t}\\right|\\right] + C",
            ).move_to(DOWN),
        ]

        self.play(Write(finalStep[0]))
        for i in range(1, len(finalStep)):
            self.play(
                TransformMatchingTex(
                    finalStep[i - 1],
                    finalStep[i],
                )
            )
            self.wait(2)

        self.play(
            FadeOut(
                miniproblemTex,
                framebox1,
                integralTex,
                step1_mini,
                framebox3,
                step1Subbed2,
                step2_mini,
                framebox5,
                step2Subbed2,
            )
        )
        self.play(finalStep[-1].animate.move_to(UP))
        finalTex = Tex("And that's the final answer ! ").next_to(
            finalStep[-1], UP, buff=0.5
        )
        framebox6 = SurroundingRectangle(finalStep[-1], buff=0.1, color=WHITE)
        self.play(Write(finalTex), FadeIn(framebox6))
        self.wait(4)
        final_finalTex = Tex(
            r"Thanks for watching.\\ Please subscribe, leave a like and have a great day!"
        ).next_to(framebox6, DOWN, buff=0.5)
        self.play(Write(final_finalTex))
        self.wait(3)
        self.play(FadeOut(finalTex, framebox6, final_finalTex, finalStep[-1]))
