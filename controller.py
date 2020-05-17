from functools import partial
import model


class PyCalcCtrl(object):
    def __init__(self, model, view):
        self._view = view
        self._evaluate = model
        self._connectSignals()
        self._clear = False

    def _calculateResult(self):
        """Evaluate expressions"""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
        self._clear = True

    def _buildExpression(self, sub_exp):

        if self._view.displayText() == model.ERROR_MSG or self._clear:
            self._view.clearDisplay()
            self._clear = False

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots"""
        for btnText, btn in self._view.buttons.items():
            if btnText not in frozenset(('=', 'C')):
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
