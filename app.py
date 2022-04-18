# 1st approach: import the entire module
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# import the entire package
# import ecommerce

# 2nd approach: import a particular function from the module in the package
# from ecommerce.shipping import calc_shipping
# calc_shipping()

# 3rd approach: import the entire module from the package
from ecommerce import shipping

shipping.calc_shipping()

# Built my own keyword checker
from kw_checker import check

print(check("try"))
