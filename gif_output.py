import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QMovie

import imageio.v3 as iio
import numpy as np

frames = np.vstack([
    iio.imread("giff 1.gif"),
    iio.imread("giff 2.gif"),
])

# get duration each frame is displayed
iio.imwrite("imageio_combined.gif", frames)

class GIFViewer(QMainWindow):
    def __init__(self, gif_path):
        super().__init__()

        self.setWindowTitle("GIF Viewer")
        self.setGeometry(100, 100, 400, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        gif_label = QLabel(self)
        layout.addWidget(gif_label)

        self.gif = QMovie(gif_path)
        gif_label.setMovie(self.gif)
        self.gif.start()

def main():
    app = QApplication(sys.argv)

    gif_path = "imageio_combined.gif"  # Replace with the path to your GIF file
    viewer = GIFViewer(gif_path)
    viewer.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
