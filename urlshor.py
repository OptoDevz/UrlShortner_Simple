import pyshorteners

custom_url = input("Enter a valid url: ")
url = pyshorteners.Shortener()
bit_url = url.tinyurl.short(str(custom_url))
print("""""
　$$　　　　$$　　$$$$$$　　$$　　　$$
　　$$　　$$　　$$　　　$$　$$　　　$$
　　　$$$$　　　$$　　　$$　$$　　　$$
　　　$$　　　　$$　　　$$　$$　　　$$
　　$$　　　　　　$$$$$$　　　$$$$$$　

　　　$$　　　$$$$$$$$　　$$$$$$$$$$
　　$$　$$　　$$　　　$$　$$　　　　
　$$　　　$$　$$$$$$$$　　$$$$$$$$$$
　$$$$$$$$$$　$$　　$$　　$$　　　　
　$$　　　$$　$$　　　$$　$$$$$$$$$$

　$$　　　　　$$               
　$$　　$$　　$$
　$$　$$　$$　$$
　$$$$　　　$$$$
　$$　　　　　$$    

　$$$$$$$$$$
　$$　　　　
　$$$$$$$$$$
　$$　　　　
　$$$$$$$$$$

　$$　　　
　$$　　　
　$$　　　
　$$　　　
　$$$$$$$$

　$$　　　
　$$　　　
　$$　　　
　$$　　　
　$$$$$$$$

　　$$$$$$　　　$$$$$$　　$$　　　　　$$　$$$$$$$$$$
　$$　　　$$　$$　　　$$　$$$$　　　$$$$　$$　　　　
　$$　　　　　$$　　　$$　$$　$$　$$　$$　$$$$$$$$$$
　$$　　　$$　$$　　　$$　$$　　$$　　$$　$$　　　　
　　$$$$$$　　　$$$$$$　　$$　　　　　$$　$$$$$$$$$$
""")
print("\n" + bit_url + "\n")
ending = input("Press enter to exit: ")
