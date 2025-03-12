from setuptools import setup, Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension(
        "pycocotools._mask",
        sources=["pycocotools/_mask.pyx"],
        include_dirs=[numpy.get_include(), '../common'],
        libraries=['m'],
        extra_compile_args=[]  # Remove -Wno-cpp here
    )
]

setup(
    name='pycocotools',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
ss
