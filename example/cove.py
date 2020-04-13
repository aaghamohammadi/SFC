import sys
import trace
import unittest
from pathlib import Path

TESTS_PATH = Path(".")
RESULTS_PATH = Path("./tmp")


def run_tests():
    suite = unittest.TestLoader().discover(start_dir=TESTS_PATH)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    tracer = trace.Trace(
        ignoredirs=[sys.prefix, sys.exec_prefix],
        trace=0,
        count=1)

    tracer.run('run_tests()')

    r = tracer.results()
    r.write_results(show_missing=True, coverdir=RESULTS_PATH)
