from PyQt5 import QtCore, QtGui, QtWidgets
import pandas
import sys


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Matchland(QtWidgets.QMainWindow):
    def __init__(self):
        super(Matchland, self).__init__()
        self.view = QtWidgets.QTableView()
        self.combo = QtWidgets.QComboBox()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.view)
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(self.vbox)

        self.data = pandas.DataFrame.from_csv('matchland.csv', index_col=None)
        self.beasts = list(self.data.keys()[4:])

        self.combo.addItems(self.beasts)
        self.display()
        self.combo.currentIndexChanged.connect(self.display)

    def display(self):
        beast = self.combo.currentText()
        result = self.data.sort_values(beast, ascending=False)[
            ['World', 'Chapter', 'Level', 'Cost'] + [beast]].dropna().astype(int)
        model = PandasModel(result)
        self.view.setModel(model)


if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = Matchland()
    window.setWindowTitle("Matchland Helper")
    window.resize(1024, 768)
    window.show()
    sys.exit(application.exec_())
