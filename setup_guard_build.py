from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "src/agd_request_guard/guard.pyx",
        compiler_directives={"language_level": "3"},
    ),
    script_args=["build_ext", "--inplace"],
)
