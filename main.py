#!/usr/bin/env python3
"""Writes the toaster error message to /output/entry.txt."""

import os

ERROR_MESSAGE = "KERNEL PANIC: The bagel is stuck. The bagel has always been stuck. The bagel is now management."  # 95 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ERROR_MESSAGE)
