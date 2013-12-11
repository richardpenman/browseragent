=====================
 agent
===========


agent.py generates a random browser user agent


Example usage: ::

    >>> import agent
    >>> 
    >>> # get a random agent from any browser
    >>> agent.rand_agent()
    'Mozilla/5.0 (X11; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0'

    >>> # get a random Firefox agent on Linux
    >>> agent.firefox_browser(agent.linux_os())
    'Mozilla/5.0 (X11; U; Linux; rv:22.0) Gecko/20100101 Firefox/22.0'

    >>> # get another random Firefox agent on Linux
    >>> agent.firefox_browser(agent.linux_os())
    'Mozilla/5.0 (X11; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0'

    >>> # get a random Chrome agent on OSX
    >>> agent.chrome_browser(agent.osx_os())
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1488.1 Safari/537.36'

    >>> # get a random Internet Explorer agent on Windows
    >>> agent.ie_browser(agent.windows_os())
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/5.0)'
