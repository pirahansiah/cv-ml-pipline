import os
import sys
import time
import json
import threading
import cv2
import numpy as np
from typing import Dict
from typing import Iterable
from typing import List


class Farshid:
    def predict(self, X: np.ndarray, names: Iterable[str] = None, meta: Dict = None) -> List[np.ndarray]:
        X = np.array(X, dtype=np.uint8)
        X = cv2.cvtColor(X, cv2.COLOR_BGR2GRAY)
        fa = X
        return [fa]
