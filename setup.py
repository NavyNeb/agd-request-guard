from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension(
        name="agd_request_guard.guard",
        sources=["src/agd_request_guard/guard.pyx"],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3", "annotation_typing": False},
    )
)
