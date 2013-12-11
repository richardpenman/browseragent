import random


# the operating system templates

def linux_os():
    dist = random.choice(['', ' U;', ' Ubuntu;'])
    system = random.choice(['', ' x86_64', ' i686'])
    return 'X11;%s Linux%s' % (dist, system)


def osx_os():
    return 'Macintosh; Intel Mac OS X 10.%d' % random.randint(6, 9)


def windows_os():
    system = random.choice(['', '; Win64; x64', '; WOW64'])
    return 'Windows NT %d.%d%s' % (random.randint(5, 6), random.randint(0, 2), system)


def rand_os():
    return random.choice([linux_os, osx_os, windows_os])()



# the browser templates

def firefox_browser(os_version):
    browser_version = random.randint(20, 25)
    return 'Mozilla/5.0 (%s; rv:%d.0) Gecko/20100101 Firefox/%d.0' % (os_version, browser_version, browser_version)

def ie_browser(os_version=None):
    os_version = windows_os() # always use windows with IE
    return 'Mozilla/5.0 (compatible; MSIE %d.0; %s; Trident/%d.0)' % (random.randint(8, 10), os_version, random.randint(5, 6))

def chrome_browser(os_version):
    return 'Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%d.0.%d.%d Safari/537.36' % (os_version, random.randint(28, 32), random.randint(1464, 1667), random.randint(0, 9))


def rand_agent():
    """Returns a random user agent across Firefox, IE, and Chrome on Linux, OSX, and Windows
    """
    browser = random.choice([firefox_browser, ie_browser, chrome_browser])
    return browser(rand_os())


if __name__ == '__main__':
    print rand_agent()
