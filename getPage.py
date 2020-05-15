import requests

blah = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# checks for errors and returns what they are
try:
    blah.raise_for_status()
except Exception as exc:
    print('There was an problem: %s' % (exc))

# checks type
type(blah)

# 200 vs 404 not found
blah.status_code == requests.codes.ok

#checks length => '178978'
len(blah.text)

# prints after slice
#print(blah.text[:250])


# creates .txt and writes it in chunks of 100000 bytes
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in blah.iter_content(100000):
    playFile.write(chunk)

playFile.close()