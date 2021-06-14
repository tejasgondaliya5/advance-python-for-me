# package is handle for folder management
'''
- 1) import Package_name.module_name
     import Package_name.Sub_Package_name.module_name

- 2) from Package_name.fu import module_name                   # this  import method is import full module
     from Package_name.Sub_Package_name import module_name

- 3) from Package_name.module_name import function_name         # this import method is import function inside module
     from Package_name.Sub_package_name.module_name import function_name

- 4) from Package_name import *                       # this not work so this solution is
     from Package_name.Sub_Package_name import *      # this not work so this solution is
          --> (__init__.py) ni Andar (__all__) name nu list banavi tema badha module name api deva na

          --> EX:-  __all__ = ['dashbord', 'service', 'product']

          import Package_name import *    # * is represent __all__ function so import module inside __all__ list
'''

