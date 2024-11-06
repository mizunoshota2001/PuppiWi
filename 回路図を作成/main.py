import os
import PyQt5
import schemdraw
import schemdraw.elements as elm

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(
    os.path.dirname(PyQt5.__file__), 'Qt5', 'plugins', 'platforms')


class FS5103B(elm.Element):
    pass


class CustomResistor(elm.Element):
    default_size = 2.0
    default_color = 'black'

    def draw(self):
        d = self.d
        d.push()
        # 抵抗のジグザグを描画
        d.move(0, 0)
        for _ in range(4):
            d += elm.Line().right().length(self.size/4)
            d += elm.Line().down().length(self.size/8)
            d += elm.Line().right().length(self.size/4)
            d += elm.Line().up().length(self.size/8)
        d.pop()
        if self.label:
            d.label(self.label, fontsize=12, color=self.color)
        return self


with schemdraw.Drawing() as d:
    d += elm.Line().right(1)
    d += elm.Resistor().right().label('R1')
    d += elm.Line().right(1)
    d += CustomResistor().right().label('R2')
    
    # d += elm.Ground(lead=False)
    # d += (Rin := elm.Resistor().at(op.in1).left().idot().label('$R_{in}$', loc='bot').label('$v_{in}$', loc='left'))
    # d += elm.Line().up(d.unit/2).at(op.in1)
    # d += elm.Resistor().tox(op.out).label('$R_f$')
    # d += elm.Line().toy(op.out).dot()
    # d += elm.Line().right(d.unit/4).at(op.out)