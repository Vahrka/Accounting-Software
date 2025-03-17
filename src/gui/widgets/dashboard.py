from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QVBoxLayout

from src.gui.widgets.base_screen import BaseScreen


class DashboardWidget(BaseScreen):

    def setup_ui(self):
        """Initialize the UI components."""

        layout = QGridLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Metrics Cards
        metrics = [
            ("Total Assets", "$152,300"),
            ("Revenue", "$89,500"),
            ("Liabilities", "$45,200"),
            ("Net Profit", "$34,800"),
        ]

        for i, (title, value) in enumerate(metrics):
            card = QFrame()
            card.setObjectName("MetricCard")
            card_layout = QVBoxLayout()
            card_layout.addWidget(QLabel(title, objectName="MetricTitle"))
            card_layout.addWidget(QLabel(value, objectName="MetricValue"))
            card.setLayout(card_layout)
            layout.addWidget(card, i // 2, i % 2)

        # Chart Placeholder
        chart_frame = QFrame()
        chart_frame.setObjectName("ChartFrame")
        chart_layout = QVBoxLayout()
        chart_layout.addWidget(QLabel("Financial Overview Chart", objectName="ChartTitle"))
        chart_frame.setLayout(chart_layout)
        layout.addWidget(chart_frame, 2, 0, 1, 2)

        self.setLayout(layout)
