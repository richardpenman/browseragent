import random


def r(low, high):
    """Shortcut for getting a random integer interval
    """
    return random.randint(low, high)


# the operating system templates

def linux():
    dist = random.choice(['', ' U;', ' Ubuntu;'])
    system = random.choice(['', ' x86_64', ' i686'])
    return 'X11;%s Linux%s' % (dist, system)


def osx():
    return 'Macintosh; Intel Mac OS X 10.%d' % r(6, 9)


def windows():
    system = random.choice(['', '; Win64; x64', '; WOW64'])
    return 'Windows NT %d.%d%s' % (r(5, 6), r(0, 2), system)


def rand_os():
    operating_systems = linux, osx, windows
    return random.choice(operating_systems)()



# the browser templates

def firefox(os_version):
    browser_version = r(20, 25)
    return 'Mozilla/5.0 (%s; rv:%d.0) Gecko/20100101 Firefox/%d.0' % (os_version, browser_version, browser_version)

def ie(os_version=None):
    os_version = windows_agent() # always use windows with IE
    return 'Mozilla/5.0 (compatible; MSIE %d.0; %s; Trident/%d.0)' % (r(8, 10), os_version, r(5, 6))

def chrome_agent(os_version):
    return 'Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%d.0.%d.%d Safari/537.36' % (os_version, r(28, 32), r(1464, 1667), r(0, 9))


def rand_agent():
    """Returns a random user agent across Firefox, IE, and Chrome on Linux, OSX, and Windows
    """
    browser = random.choice([firefox, ie, chrome])
    return browser(rand_os())


if __name__ == '__main__':
    print rand_agent()
