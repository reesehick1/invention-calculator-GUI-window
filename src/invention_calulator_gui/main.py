"""
this took so many tutorials...
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QCalendarWidget,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Invention Calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(350, 600) 

        layout = QVBoxLayout()

        self.title_label = QLabel("Select Start Date:")
        font = self.title_label.font()
        font.setPointSize(12)
        self.title_label.setFont(font)
        self.calendar1 = QCalendarWidget()

        self.end_date_label = QLabel("Select End Date:")
        self.end_date_label.setFont(font)
        self.calendar2 = QCalendarWidget()

        submit_button = QPushButton("Compare Dates")
        submit_button.clicked.connect(self.process_date)

        self.result_label = QLabel("")
        self.result_label.setFont(font)

        layout.addWidget(self.title_label)
        layout.addWidget(self.calendar1)
        layout.addWidget(self.end_date_label)
        layout.addWidget(self.calendar2)
        layout.addWidget(submit_button)
        layout.addWidget(self.result_label)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def process_date(self):
        start_qdate = self.calendar1.selectedDate()
        end_qdate = self.calendar2.selectedDate()

        if start_qdate > end_qdate:
            earlier_date = end_qdate
            later_date = start_qdate
        else:
            earlier_date = start_qdate
            later_date = end_qdate

        years = 0
        while earlier_date.addYears(1) <= later_date:
            earlier_date = earlier_date.addYears(1)
            years += 1

        months = 0
        while earlier_date.addMonths(1) <= later_date:
            earlier_date = earlier_date.addMonths(1)
            months += 1

        days = earlier_date.daysTo(later_date)

        formatted_result = f"The Difference Is: {years:04d}-{months:02d}-{days:02d}"
        self.result_label.setText(formatted_result)
   
        print(f"Start: {start_qdate.toString('yyyy-MM-dd')}")
        print(f"End: {end_qdate.toString('yyyy-MM-dd')}")
        print(formatted_result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()