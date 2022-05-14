import urllib2
response = urllib2.urlopen('https://pp.vk.me/c540104/c624218/v624218602/3321/uYVa4FQv_q0.jpg')
content = response.read()
file = open('image.jpg', 'w')
file.write(content)
file.close()