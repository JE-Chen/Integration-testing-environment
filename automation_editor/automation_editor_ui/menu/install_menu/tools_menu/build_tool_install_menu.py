from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtGui import QAction

from automation_editor.automation_editor_ui.menu.install_menu.install_utils import install_package

if TYPE_CHECKING:
    from automation_editor.automation_editor_ui.editor_main.main_ui import AutomationEditor


def build_tool_install_menu(ui_we_want_to_set: AutomationEditor):
    ui_we_want_to_set.install_tools_menu = ui_we_want_to_set.install_menu.addMenu("Tools")
    # Try to install Build Tools
    ui_we_want_to_set.install_tool_action = QAction("Install Build Tools")
    ui_we_want_to_set.install_tool_action.triggered.connect(
        lambda: install_build_tools(ui_we_want_to_set)
    )
    ui_we_want_to_set.install_tools_menu.addAction(ui_we_want_to_set.install_tool_action)


def install_build_tools(ui_we_want_to_set: AutomationEditor) -> None:
    install_package("setuptools", ui_we_want_to_set)
    install_package("build", ui_we_want_to_set)
    install_package("wheel", ui_we_want_to_set)
