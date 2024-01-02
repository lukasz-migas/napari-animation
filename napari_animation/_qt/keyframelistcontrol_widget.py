"""Qt widget for controlling a KeyFrameListWidget."""
from __future__ import annotations

from typing import TYPE_CHECKING

from qtpy.QtWidgets import QFrame, QHBoxLayout, QPushButton


if TYPE_CHECKING:
    from ..animation import Animation


class KeyFrameListControlWidget(QFrame):
    """Controls for a KeyFrameListWidget"""

    def __init__(self, animation: Animation, parent=None):
        super().__init__(parent=parent)
        self.animation = animation

        layout = QHBoxLayout()
        self.captureButton = KeyFrameCaptureButton(self.animation)
        self.deleteButton = KeyFrameDeleteButton(self.animation)
        layout.addWidget(self.captureButton)
        layout.addWidget(self.deleteButton)
        self.setLayout(layout)


class KeyFrameDeleteButton(QPushButton):
    """Delete selected key-frame."""

    def __init__(self, animation: Animation):
        super().__init__()

        self.animation = animation
        self.setToolTip("Delete selected key-frame")
        self.setText("Delete")

        self.setEnabled(bool(self.animation.key_frames))


class KeyFrameCaptureButton(QPushButton):
    """Capture current viewer state as a key-frame."""

    def __init__(self, animation: Animation):
        super().__init__()

        self.animation = animation
        self.setToolTip("Capture key-frame")
        self.setText("Capture")
