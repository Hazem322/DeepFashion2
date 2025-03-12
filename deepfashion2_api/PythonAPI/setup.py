from setuptools import setup, Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        name='pycocotools._mask',
        sources=['pycocotools/_mask.pyx'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    ),
]

setup(
    name='pycocotools',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
