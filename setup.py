from setuptools import setup, find_packages

setup(
    name='easyraspberry',
    version='0.1',
    packages=find_packages(),  # Automatycznie znajdzie wszystkie pakiety w projekcie
    description='Easy to use Raspberry Pi GPIO library',  
    author='Kot Pasztet',
    author_email='gdylf.pl@gmail.com',
    install_requires=[
        'adafruit-circuitpython-st7735r==2.0.0',
        'Adafruit-Blinka==8.56.0',
        'Adafruit-PlatformDetect==3.77.0',
        'Adafruit-PureIO==1.1.11',
        'binho-host-adapter==0.1.6',
        'pyserial==3.5',
        'pyftdi==0.56.0',
        'pyusb==1.3.1',
        'RPi.GPIO==0.7.1',
        'rpi-ws281x==5.0.0',
        'sysv-ipc==1.1.0',
        'adafruit-circuitpython-typing==1.11.2',
        'adafruit-circuitpython-busdevice==5.2.11',
        'adafruit-circuitpython-requests==4.1.10',
        'typing_extensions==4.12.2',
        'adafruit-blinka-displayio==2.1.7',
        'adafruit-circuitpython-bitmap_font==2.2.0',
    ],
    python_requires='>=3.6',  # Jeśli używasz Pythona w wersji 3.6 i wyższej
)
