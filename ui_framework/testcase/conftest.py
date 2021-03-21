import os
import signal
import subprocess

import pytest

from ui_framework.page.logger import log_init


@pytest.fixture(scope="module",autouse=True)
def record():
    log_init()
    cmd = 'scrcpy -Nr tmp.mp4'
    p = subprocess.Popen(cmd,shell=True)
    yield
    #运行测试用例后做的一些事
    os.kill(p.pid,signal.CTRL_C_EVENT)