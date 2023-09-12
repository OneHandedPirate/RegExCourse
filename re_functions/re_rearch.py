import re


print(result[0] if (result := re.search(r'#[a-z]+', input())) else 'There are no hashtags :(')
