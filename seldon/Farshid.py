
#
# import argparse
import os
import sys
import time
import json
import threading
# import signal
# import datetime
# import traceback
# import subprocess
import cv2
# import imutils
# import numpy as np

import numpy as np
from typing import Dict
from typing import Iterable
from typing import List


class Farshid:
    # def predict(self, X: np.ndarray, names: Iterable[str] = None, meta: Dict = None) -> List[str]:
    #payload = {"data": {"tensor": {"shape": fa.shape, "values": fa.reshape(-1).tolist()}}}
    def predict(self, X: np.ndarray, names: Iterable[str] = None, meta: Dict = None) -> List[np.ndarray]:
        # np.ndarray
        X = np.array(X, dtype=np.uint8)
        X = cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)
        fa = X
        #fa = ["asdfsaf"]
        #fa = X
        return [fa]  # .tolist()

    # class Test:
    #     def predict(self, names: str):
    #         return [names]
