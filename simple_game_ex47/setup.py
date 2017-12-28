try:
    from setuptools import setup

    except ImportError:
        from distutils.core import setup

    config = [
        'description': 'My Project',
        'author': 'David Lynch',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'davelynch45@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'game'
    ]
 
    setup(**config)
