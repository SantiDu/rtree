# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
# try:
#     __import__('pkg_resources').declare_namespace(__name__)
# except ImportError:
#     from pkgutil import extend_path
#     __path__ = extend_path(__path__, __name__)

from index import Rtree

from core import rt

__version__ = '0.7.0'