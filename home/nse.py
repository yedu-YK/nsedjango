from nsetools import Nse


nse = Nse()



data = nse.get_quote('sbin')
# print(data.keys())

for k in data.keys():
    print(k)